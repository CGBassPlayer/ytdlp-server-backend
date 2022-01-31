from typing import List

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.db.models.task import Task
from backend.db.models.ytdlp_config import YtdlpConfig
from backend.db.session import get_db
from backend.schemas.task import TaskCreate
from backend.schemas.ytdlp_config import YtdlpConfigGet, YtdlpConfigUpdate, YtdlpConfigCreate

router = APIRouter()


@router.get("/config", response_model=List[YtdlpConfigGet])
async def get_configs(db: Session = Depends(get_db)):
    """
    Get all the configuration settings from the database
    """
    configs = db.query(YtdlpConfig).all()
    if not configs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No configurations were found")
    return configs


@router.post("/config", response_model=YtdlpConfigCreate)
async def create_config(config: YtdlpConfigCreate, db: Session = Depends(get_db)):
    """
    Create a new configuration parameter
    """
    db_config = YtdlpConfigCreate(flag=config.flag, value=config.value, enabled=True)
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config


@router.put("/config")
async def update_config(config: YtdlpConfigUpdate, db: Session = Depends(get_db)):
    """
    Update configuration parameter
    """
    old_config: YtdlpConfig = db.query(YtdlpConfig).get(config.flag)

    if not old_config:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Configuration {config.flag} was not found")

    if config.value is not None:
        old_config.value = config.value
    old_config.enabled = config.enabled

    db.commit()
    return {
        "code": "success",
        "config": config
    }


@router.get("/task")
async def get_tasks(db: Session = Depends(get_db)):
    """
    Get all tasks
    """
    tasks = db.query(Task).all()

    if not tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No tasks found!")

    return tasks


@router.post("/task")
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task
    """
    new_task = Task(tid=task.tid, url=task.url, state=task.state, valid=task.valid, title=task.title,
                    create_time=task.create_time, finish_time=task.finish_time, format=task.format, ext=task.ext,
                    thumbnail=task.thumbnail, duration=task.duration, view_count=task.view_count,
                    like_count=task.like_count, dislike_count=task.dislike_count, average_rating=task.average_rating,
                    description=task.description)

    db_task = db.query(Task).filter(Task.tid == task.tid).first()
    if db_task is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Task id {task.tid} already exists")

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
