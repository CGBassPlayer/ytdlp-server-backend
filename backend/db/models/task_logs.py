from sqlalchemy import Column, String, Integer, func
from sqlalchemy.orm import relationship

from backend.db.base import Base


class TaskLogs(Base):
    __tablename__ = "task_logs"

    tid = Column(String, nullable=False, primary_key=True)
    log_timestamp = Column(String, nullable=False, primary_key=True, default=func.now(tz="America/New_York"))
    level = Column(Integer, nullable=False, default=3)
    message = Column(String, nullable=False)
    task = relationship("Task")

    def __init__(self, tid, message, level=3):
        self.tid = tid
        self.level = level
        self.message = message

    def __repr__(self):
        return f"<TaskLog(tid: {self.tid}, timestamp: {self.log_timestamp}, level: {self.level}, message: {self.message})>"
