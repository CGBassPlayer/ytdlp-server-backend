from typing import Optional

from pydantic import BaseModel


class TaskLogsBase(BaseModel):
    message: str


class TaskLogsGet(TaskLogsBase):
    timestamp: str
    level: str

    class Config:
        orm_mode: True


class TaskLogsCreate(TaskLogsBase):
    tid: str
    level: Optional[int]
