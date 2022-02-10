from sqlalchemy.orm import Session

from backend.db.models.status import Status


def get_message(status: int, db: Session):
    return db.query(Status).filter(Status.status == status).first().message
