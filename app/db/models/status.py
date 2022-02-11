from sqlalchemy import Column, String, Integer

from app.db.base import Base


class Status(Base):
    __tablename__ = "status"

    status = Column(Integer, nullable=False, primary_key=True)
    message = Column(String, nullable=False)

    def __repr__(self):
        return f"<Task(status: {self.status}, message: {self.message})>"
