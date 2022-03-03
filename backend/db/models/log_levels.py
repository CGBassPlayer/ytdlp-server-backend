from sqlalchemy import Column, String, Integer

from backend.db.base import Base


class LogLevel(Base):
    __tablename__ = "log_levels"

    level_code = Column(Integer, nullable=False, primary_key=True)
    level_name = Column(String, nullable=False)

    def __repr__(self):
        return f"<LogLevel(code: {self.level_code}, name: {self.level_name})>"
