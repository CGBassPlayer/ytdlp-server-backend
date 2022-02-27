from sqlalchemy.orm import Session

from backend.db.models.status import Status


def get_message(status: int, db: Session) -> str:
    """
    Get the name of the status code

    :param status: status code
    :param db: connection to the database
    :return: status message
    """
    return db.query(Status).filter(Status.status == status).first().message
