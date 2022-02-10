from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from backend.db.base import Base


class Video(Base):
    __tablename__ = "video"

    vid = Column(String, nullable=False, primary_key=True)
    platform = Column(String, nullable=False)
    url = Column(String, nullable=False)
    title = Column(String)
    description = Column(String)
    task = relationship("Task")

    def __repr__(self):
        return f"<Video(id: {self.vid}, platform: {self.platform}, url: {self.url}, title: {self.title})>"
