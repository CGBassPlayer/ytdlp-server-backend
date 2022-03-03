from typing import Optional

from pydantic import BaseModel


class VideoBase(BaseModel):
    url: str
    title: Optional[str]
    description: Optional[str]


class VideoGet(VideoBase):
    vid: str
    platform: str

    class Config:
        orm_mode = True


class VideoCreate(VideoBase):
    vid: Optional[str]
