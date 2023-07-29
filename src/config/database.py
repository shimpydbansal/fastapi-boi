import os
import sys
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from config.logger import logger
from src.common.base_model import BaseModel  # noqa: F401

from .env import settings

# import logging
# logging.basicConfig(level=logging.INFO)


current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), pool_pre_ping=True)
with engine.connect() as connection:
    connection.execute(text('set search_path to "%s"' % settings.DB_SCHEMA))
    connection.commit()

DatabaseSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session() -> Generator:
    try:
        db = DatabaseSession()
        yield db
    finally:
        db.close()


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    BaseModel.metadata.create_all(bind=engine)

    # Create a session
    # Session = sessionmaker(bind=engine)
    # session = Session()


def get_db_connection_status():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        logger.info("Database connection is successful.")
        return True
    except Exception as e:
        logger.exception("Database connection failed. Error details: ", str(e))
        return False
