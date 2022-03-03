import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME = "YT-DLP Server"
    PROJECT_VERSION = "0.1.0"

    DATABASE_TYPE: str = os.getenv("DB_TYPE")
    DATABASE_USER: str = os.getenv("DB_USER")
    DATABASE_PASSWORD: str = os.getenv("DB_PASS")
    DATABASE_SERVER: str = os.getenv("DB_SERVER")
    DATABASE_PORT: str = os.getenv("DB_PORT")
    DATABASE_DB: str = os.getenv("DB_DB")
    DATABASE_URL = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_SERVER}:{DATABASE_PORT}/{DATABASE_DB}"
    SQLITE_DB = "sqlite:///ytdlp-server.sqlite3"

    LOG_LEVEL = 3


settings = Settings()
