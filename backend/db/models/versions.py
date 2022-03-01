from sqlalchemy import Column, String

from backend.db.base import Base


class Version(Base):
    __tablename__ = "versions"

    id = Column(String, nullable=False, primary_key=True)
    updated = Column(String)
    status = Column(String, nullable=False)
    link = Column(String, nullable=False)
