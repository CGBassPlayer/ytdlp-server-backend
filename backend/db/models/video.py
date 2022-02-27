from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from yt_dlp import YoutubeDL

from backend.db.base import Base


class Video(Base):
    __tablename__ = "video"

    vid = Column(String, nullable=False, primary_key=True)
    platform = Column(String, nullable=False)
    url = Column(String, nullable=False)
    title = Column(String)
    description = Column(String)
    upload_date = Column(String, nullable=False)
    uploader = Column(String, nullable=False)
    duration = Column(String, nullable=False, default="0:00")
    thumbnail = Column(String)
    task = relationship("Task")

    def __init__(self, url: str) -> None:
        self.url = url
        with YoutubeDL() as ydl:
            info_dict = ydl.extract_info(self.url, download=False)
            self.vid = info_dict.get("id")
            self.platform = info_dict.get("webpage_url_domain")
            self.title = info_dict.get("title")
            self.description = info_dict.get("description")
            self.upload_date = info_dict.get("upload_date")
            self.uploader = info_dict.get("uploader")
            self.duration = info_dict.get("duration_string")
            self.thumbnail = info_dict.get("thumbnail")

    def __repr__(self):
        return f"<Video(id: {self.vid}, platform: {self.platform}, url: {self.url}, title: {self.title})>"
