from sqlalchemy.orm import Session

from app.db.models.status import Status


def get_message(status: int, db: Session):
    return db.query(Status).filter(Status.status == status).first().message


def generate_task_id(vid):
    pass
