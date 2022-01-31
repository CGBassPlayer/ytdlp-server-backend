from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

from backend.db.base import Base


class TaskStatus(Base):
    __tablename__ = "task_status"

    tid = Column(String, nullable=False, primary_key=True)
    percent = Column(String, nullable=False, default="0.0%")
    filename = Column(String)
    tmp_filename = Column(String)
    download_bytes = Column(Integer, default=0),
    total_bytes = Column(Integer, default=0),
    total_bytes_estimate = Column(Integer, default=0)
    speed = Column(Integer, default=0)
    eta = Column(Integer, default=0)
    elapsed = Column(Integer, default=0)
    start_time = Column(DateTime, default=0.0)
    pause_time = Column(DateTime, default=0.0)
    logs = Column(String, nullable=False, default='[]')

    task_ids = relationship("TaskStatus", back_populates="tasks")

    def __init__(self, tid, percent, filename, tmp_filename, download_bytes, total_bytes, total_bytes_estimate, speed,
                 eta, elapsed, start_time, pause_time, logs):
        self.tid = tid
        self.percent = percent
        self.filename = filename
        self.tmp_filename = tmp_filename,
        self.download_bytes = download_bytes
        self.total_bytes = total_bytes
        self.total_bytes_estimate = total_bytes_estimate
        self.speed = speed
        self.eta = eta
        self.elapsed = elapsed
        self.start_time = start_time
        self.pause_time = pause_time
        self.logs = logs

    def __repr__(self):
        return f"<TaskStatus(tid: {self.tid}, filename: {self.filename})>"
