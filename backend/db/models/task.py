import time
from xmlrpc.client import DateTime

from sqlalchemy import Column, String, Integer, func

from backend.db.base import Base


class Task(Base):
    __tablename__ = "task"

    tid = Column(String, nullable=False, primary_key=True)
    url = Column(String, nullable=False)
    state = Column(Integer, nullable=False, default=2)
    valid = Column(Integer, nullable=False, default=0)
    title = Column(String)
    create_time = Column(DateTime, nullable=False, default=func.current_timestamp)
    finish_time = Column(DateTime)
    format = Column(String)
    ext = Column(String)
    thumbnail = Column(String)
    duration = Column(String)
    view_count = Column(String)
    like_count = Column(String)
    dislike_count = Column(String)
    average_rating = Column(String)
    description = Column(String)

    def __init__(self, tid, url, state, valid, title, create_time, finish_time, format, ext, thumbnail, duration,
                 view_count, like_count, dislike_count, average_rating, description):
        self.tid = tid
        self.url = url
        self.state = state
        self.valid = valid
        self.title = title
        self.create_time = create_time
        self.finish_time = finish_time
        self.format = format
        self.thumbnail = thumbnail
        self.duration = duration
        self.view_count = view_count
        self.like_count = like_count
        self.dislike_count = dislike_count
        self.average_rating = average_rating
        self.description = description

    def __repr__(self):
        return f"<Task(id: {self.tid}, url: {self.url}, state: {self.state}, title: {self.title})>"
