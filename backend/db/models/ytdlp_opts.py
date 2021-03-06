from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from backend.db.base import Base


class YtdlpOpt(Base):
    __tablename__ = "ytdlp_opt"

    tid = Column(String, nullable=False, primary_key=True)
    options = Column(String)
    task = relationship("Task")

    def __init__(self, tid, options):
        self.tid: str = tid
        self.options = options

    def __repr__(self):
        return f"<YtdlpOpt(tid: {self.tid}, options: {self.options})>"
