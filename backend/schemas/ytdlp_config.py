from typing import Optional

from pydantic import BaseModel


class YtdlpConfigBase(BaseModel):
    flag: str
    value: Optional[str]


class YtdlpConfigGet(YtdlpConfigBase):
    enabled: bool

    class Config:
        orm_mode = True


class YtdlpConfigCreate(YtdlpConfigBase):
    pass


class YtdlpConfigUpdate(YtdlpConfigBase):
    enabled: bool
