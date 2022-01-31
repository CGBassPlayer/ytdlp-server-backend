from typing import Optional

from pydantic import BaseModel


class TaskBase(BaseModel):
    tid: str
    url: str
    state: int
    valid: Optional[int]
    title: Optional[str]
    create_time: Optional[int]
    finish_time: Optional[int]
    format: Optional[str]
    ext: Optional[str]
    thumbnail: Optional[str]
    duration: Optional[str]
    view_count: Optional[str]
    like_count: Optional[str]
    dislike_count: Optional[str]
    average_rating: Optional[str]
    description: Optional[str]


class TaskGet(TaskBase):
    pass


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass
