from typing import Optional

from pydantic import BaseModel
from pydantic.schema import datetime

from backend.schemas.video import VideoGet


class TaskBase(BaseModel):
    tid: str


class TaskGet(TaskBase):
    video: Optional[VideoGet]
    create_date: datetime
    finish_date: Optional[datetime]
    status: int
    percent: str
    filename: Optional[str]
    logs: str

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    vid: str


class TaskUpdate(TaskBase):
    vid: Optional[str]
    status: Optional[str]
    filename: Optional[str]
