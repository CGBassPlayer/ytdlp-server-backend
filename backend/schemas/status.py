from pydantic import BaseModel


class StatusBase(BaseModel):
    status: int
    message: str


class StatusGet(StatusBase):
    pass
