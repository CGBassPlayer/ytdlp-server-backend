from typing import List

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.apis.utils import get_message
from backend.db.models.status import Status
from backend.db.models.task import Task
from backend.db.models.video import Video
from backend.db.models.ytdlp_opts import YtdlpOpt
from backend.db.session import get_db
from backend.schemas.status import StatusGet
from backend.schemas.task import TaskGet, TaskCreate
from backend.schemas.video import VideoGet
from backend.schemas.ytdlp_opts import YtdlpOptGet, YtdlpOptUpdate

router = APIRouter()


@router.get("/config/{task_id}", response_model=List[YtdlpOptGet])
async def get_config(task_id: str, db: Session = Depends(get_db)):
    """
    Get all the configuration settings from the database
    """
    db_config: YtdlpOptGet = db.query(YtdlpOpt).filter(YtdlpOpt.tid == task_id).all()
    print(db_config)
    if not db_config:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No configuration was found for {task_id}")
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
    old_config.options = config.options
    db.commit()
    db_status: StatusGet = db.query(Status).filter(Status.message == "succeeded").first()
    return {
        "status": db_status.message,
        "config": config
    }


@router.get("/video/{video_id}")
async def get_video(video_id: str, db: Session = Depends(get_db)):
    """
    Get details of a task by its id
    """
    db_video: Video = db.query(Video).filter(Video.vid == video_id).first()
    if not db_video:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No video was found for {video_id}")
    return db_video


@router.get("/task/{task_id}", response_model=TaskGet)
async def get_task(task_id: str, db: Session = Depends(get_db)):
    """
    Get details of a task by its id
    """
    db_task = db.query(Task).filter(Task.tid == task_id).first()
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No task was found for {task_id}")
    db_video = db.query(Video).filter(Video.vid == db_task.vid).first()
    if not db_video:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No video was found for {db_task.vid}")
    return TaskGet(tid=db_task.tid,
                   video=VideoGet(
                       vid=db_task.vid,
                       platform=db_video.platform,
                       url=db_video.url,
                       title=db_video.title,
                       description=db_video.description
                   ),
                   create_date=db_task.create_date,
                   finish_date=db_task.finish_date,
                   status=get_message(db_task.status, db),
                   percent=db_task.percent,
                   filename=db_task.filename,
                   logs=db_task.logs)


@router.post("/task")
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(tid=task.tid,
                   vid=task.vid,
                   status=1)
    if not task.config:
        task.config = db.query(YtdlpOpt).filter(YtdlpOpt.tid == "<global>").first().options
        db_task.logs = "Using global configuration::"
    db_opts = YtdlpOpt(tid=task.tid,
                       options=task.config)
    db.add(db_task)
    db.add(db_opts)
    db.commit()
    return db_task
