from typing import Optional, List

from pydantic import BaseModel
from pydantic.schema import datetime

from backend.schemas.task_logs import TaskLogsGet
from backend.schemas.video import VideoGet


class TaskBase(BaseModel):
    pass


class TaskGet(TaskBase):
    tid: str
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
    url: str
    config: Optional[List[str]]


class TaskUpdate(TaskBase):
    tid: str
    vid: Optional[str]
    status: Optional[str]
    filename: Optional[str]
