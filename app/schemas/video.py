from typing import Optional

from pydantic import BaseModel


class VideoBase(BaseModel):
    vid: str
    platform: str
    url: str


class VideoGet(VideoBase):
    title: Optional[str]
    description: Optional[str]

    class Config:
        orm_mode = True


class VideoCreate(VideoBase):
    title: Optional[str]
    description: Optional[str]
