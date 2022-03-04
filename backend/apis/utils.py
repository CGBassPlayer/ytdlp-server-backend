from sqlalchemy.orm import Session

from backend.db.models.log_levels import LogLevel
from backend.db.models.status import Status


def get_status_message(status: int, db: Session) -> str:
    """
    Get the name of the status code

    :param status: status code
    :param db: connection to the database
    :return: status message
    """
    return db.query(Status).filter(Status.status == status).first().message


def log_level_to_str(log_level: int, db: Session):
    lvl: LogLevel = db.query(LogLevel).filter(LogLevel.level_code == log_level).first()
    return lvl.level_name


def log_level_to_int(log_level: str, db: Session):
    lvl: LogLevel = db.query(LogLevel).filter(LogLevel.level_name == log_level.strip().upper()).first()
    return lvl.level_code
