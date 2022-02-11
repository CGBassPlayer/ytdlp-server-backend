from typing import Optional, List

from pydantic import BaseModel
from pydantic.schema import datetime

from app.schemas.task_logs import TaskLogsGet
from app.schemas.video import VideoGet


class TaskBase(BaseModel):
    tid: str


class TaskGet(TaskBase):
    video: VideoGet
    create_date: datetime
    finish_date: Optional[datetime]
    status: str
    percent: str
    filename: Optional[str]
    logs: Optional[List[TaskLogsGet]]

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    vid: str
    config: Optional[List[str]]


class TaskUpdate(TaskBase):
    vid: Optional[str]
    status: Optional[str]
    filename: Optional[str]
