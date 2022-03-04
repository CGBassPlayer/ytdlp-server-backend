from typing import Optional, List

from pydantic import BaseModel
from pydantic.schema import datetime

from backend.apis import utils
from backend.db.models.task import Task as TaskModel
from backend.db.models.task_logs import TaskLogs as TaskLogsModel
from backend.db.models.video import Video as VideoModel
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


def to_TaskGet(db, task_model: TaskModel, video_model: VideoModel, logs_model: List[TaskLogsModel] = None) -> TaskGet:
    logs = []
    if logs_model is not None:
        for log in logs_model:
            logs.append(TaskLogsGet(timestamp=log.log_timestamp,
                                    level=utils.log_level_to_str(log.level, db),
                                    message=log.message))

    return TaskGet(tid=task_model.tid,
                   video=VideoGet(vid=task_model.vid,
                                  platform=video_model.platform,
                                  url=video_model.url,
                                  title=video_model.title,
                                  description=video_model.description),
                   create_date=task_model.create_date,
                   finish_date=task_model.finish_date,
                   status=utils.get_status_message(task_model.status, db),
                   percent=task_model.percent,
                   filename=task_model.filename,
                   logs=logs)
