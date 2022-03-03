import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func, Float

from backend.db.base import Base


class Task(Base):
    __tablename__ = "task"

    tid = Column(String, ForeignKey("ytdlp_opt.tid"), ForeignKey("task_logs.tid"), nullable=False, primary_key=True)
    vid = Column(String, ForeignKey("video.vid"), nullable=False)
    create_date = Column(DateTime, nullable=False, server_default=func.now(tz="America/New_York"))
    finish_date = Column(DateTime)
    status = Column(Integer, nullable=False)
    percent = Column(Float, nullable=False, default=0.0)
    filename = Column(String)

    def __init__(self, vid: str, status: int) -> None:
        self.vid = vid
        self.status = status
        self.create_date = datetime.datetime.now()
        if self.tid is None:
            self.generate_task_id()
        super().__init__()

    def __repr__(self):
        return f"<Task(id: {self.tid}, video_id: {self.vid}, create_date: {self.create_date}, status: {self.status})>"

    def generate_task_id(self):
        self.tid = f"{self.create_date}-{self.vid}"
