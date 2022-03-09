from typing import List

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.apis import utils
from backend.core.config import settings
from backend.db.models.status import Status
from backend.db.models.task import Task
from backend.db.models.task_logs import TaskLogs
from backend.db.models.video import Video
from backend.db.models.ytdlp_opts import YtdlpOpt
from backend.db.session import get_db
from backend.schemas.status import StatusGet
from backend.schemas.task import TaskGet, TaskCreate, to_TaskGet
from backend.schemas.ytdlp_opts import YtdlpOptGet, YtdlpOptUpdate

router = APIRouter()


@router.get("/config", response_model=List[YtdlpOptGet])
async def get_config(tid: str = None, db: Session = Depends(get_db)):
    """
    Get all the configuration settings from the database
    """
    if tid:
        db_config: YtdlpOptGet = db.query(YtdlpOpt).filter(YtdlpOpt.tid == tid).all()
    else:
        db_config: YtdlpOptGet = db.query(YtdlpOpt).all()
    if not db_config:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No configuration was found for {tid}")
    return db_config


@router.put("/config")
async def update_config(config: YtdlpOptUpdate, db: Session = Depends(get_db)):
    """
    Update configuration parameter
    """
    old_config: YtdlpOpt = db.query(YtdlpOpt).get(config.tid)
    if not old_config:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Configuration for task {config.tid} was not found")
    old_config.options = config.options.__str__()
    db.commit()
    db_status: StatusGet = db.query(Status).filter(Status.message == "succeeded").first()
    return {
        "status": db_status.message,
        "config": config
    }


@router.get("/video/")
async def get_video(vid: str = None, db: Session = Depends(get_db)):
    """
    Get details of a task by its id
    """
    if vid:
        db_video: Video = db.query(Video).filter(Video.vid == vid).first()
    else:
        db_video: Video = db.query(Video).all()
    if not db_video:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No video was found for {vid}")
    return db_video


@router.get("/task/all", response_model=List[TaskGet])
async def get_all_tasks(log_level=settings.LOG_LEVEL, db: Session = Depends(get_db)):
    """
    Get all tasks that are not skipped or completed successfully
    """
    if not log_level.isdigit():
        log_level = utils.log_level_to_int(log_level, db)
    db_tasks: List[Task] = db.query(Task).filter(Task.status != 4 or Task.status != 5).all()
    tasks = []
    for db_task in db_tasks:
        db_video: Video = db.query(Video).filter(Video.vid == db_task.vid).first()
        db_logs = db.query(TaskLogs).filter(TaskLogs.tid == db_task.tid, TaskLogs.level >= log_level).all()
        tasks.append(to_TaskGet(db, db_task, db_video, db_logs))
    return tasks


@router.get("/task", response_model=TaskGet)
async def get_task(tid: str, log_level=settings.LOG_LEVEL, db: Session = Depends(get_db)):
    """
    Get details of a task by its id
    """
    if not log_level.isdigit():
        log_level = utils.log_level_to_int(log_level, db)
    db_task = db.query(Task).filter(Task.tid == tid).first()
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No task was found for {tid}")
    db_video = db.query(Video).filter(Video.vid == db_task.vid).first()
    if not db_video:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No video was found for {db_task.vid}")
    db_logs = db.query(TaskLogs).filter(TaskLogs.tid == tid, TaskLogs.level >= log_level).all()
    return to_TaskGet(db, db_task, db_video, db_logs)


@router.post("/task")
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_video = db.query(Video).filter(Video.url == task.url).first()
    if not db_video:
        new_video = Video(url=task.url)
        db.add(new_video)
        db.commit()
        db_video = db.query(Video).filter(Video.url == task.url).first()
    db_task = Task(vid=db_video.vid,
                   status=1)
    if not task.config:
        task.config = db.query(YtdlpOpt).filter(YtdlpOpt.tid == "<global>").first().options
        db_log = TaskLogs(tid=db_task.tid,
                          message="global configuration loaded for this task")
        db.add(db_log)
    db_opts = YtdlpOpt(tid=db_task.tid,
                       options=task.config.__str__())

    db_existing_task = db.query(Task).filter(Video.vid == db_video.vid).filter(
        YtdlpOpt.options == db_opts.options).first()
    if db_existing_task:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="task with this config already exists")

    db.add(db_task)
    db.add(db_opts)
    db.commit()
    return {"message": "success"}
