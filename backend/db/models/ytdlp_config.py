from sqlalchemy import Boolean, Column, String

from backend.db.base import Base


class YtdlpConfig(Base):
    __tablename__ = "ytdlp_config"

    flag = Column(String, primary_key=True)
    value = Column(String)
    enabled = Column(Boolean, default=True)

    def __init__(self, flag, value, enabled):
        self.flag: str = flag
        self.value = value
        self.enabled: bool = enabled

    def __repr__(self):
        return f"<YtdlpConfig(flag: {self.flag}, value: {self.value}, enabled: {self.enabled})>"
