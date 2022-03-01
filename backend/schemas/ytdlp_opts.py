from typing import Optional, List

from pydantic import BaseModel


class YtdlpOptBase(BaseModel):
    tid: str


class YtdlpOptGet(YtdlpOptBase):
    options: Optional[str]

    class Config:
        orm_mode = True


class YtdlpOptCreate(YtdlpOptBase):
    options: str


class YtdlpOptUpdate(YtdlpOptBase):
    options: List[str]
