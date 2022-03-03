from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # to generate table name from classname
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()
