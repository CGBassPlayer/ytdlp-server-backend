from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func

from backend.db.base import Base


class Task(Base):
    __tablename__ = "task"

    tid = Column(String, ForeignKey("ytdlp_opt.tid"), ForeignKey("task_logs.tid"), nullable=False, primary_key=True)
    vid = Column(String, ForeignKey("video.vid"), nullable=False)
    create_date = Column(DateTime, nullable=False, server_default=func.now())
    finish_date = Column(DateTime)
    status = Column(Integer, nullable=False)
    percent = Column(String, nullable=False, default="0.0%")
    filename = Column(String)

    def __repr__(self):
        return f"<Task(id: {self.tid}, video_id: {self.vid}, create_date: {self.create_date}, status: {self.status})>"
