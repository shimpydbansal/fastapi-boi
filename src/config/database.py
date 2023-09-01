"""
This module handles database connections and sessions for the application.

It defines the database engine and session factory, and provides functions
for creating and managing sessions, initializing the database, and checking
the database connection status.

Functions:
    - get_db_session(): Generator function for creating and managing a
    database session.
    - init_db(db: Session): Initialize the database, creating all tables
    defined in the BaseModel.
    - get_db_connection_status(): Check the database connection status.

Imported:
    - os, sys: For file path manipulations.
    - Generator: For typing.
    - create_engine, text, Session, sessionmaker: SQLAlchemy functions and
    classes.
    - logger: Application logger.
    - BaseModel: Base class for database models.
    - settings: Environment settings.
"""

import os
import sys
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy import text

# from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from common.base_model import BaseModel  # noqa: F401
from config.env import settings
from config.logger import logger
from module.user.user_model import UserModel  # noqa: F401

# Set the current directory path
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


# import logging
# logging.basicConfig(level=logging.INFO)

# Create the database engine
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI, echo=True, pool_pre_ping=True
)
with engine.connect() as connection:
    connection.execute(text('set search_path to "%s"' % settings.DB_SCHEMA))
    connection.commit()

DatabaseSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session() -> Generator:
    """
    Create and manages a database session.

    Yields:
        Generator: A SQLAlchemy database session object.

    Note:
        The session is automatically closed when the generator is exhausted.
    """
    db = DatabaseSession()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """
    Initialize the database, creating all tables defined in the BaseModel.

    Note:
        Tables should be created with Alembic migrations. If you don't want to
        use migrations,
        create the tables by un-commenting the line that creates the tables.
    """
    # Tables should be created with Alembic migrations
    # But for development purposes,
    # database changes will be done by this block.
    if settings.ENVIRONMENT == "development":
        logger.info("Initializing database...")
        try:
            BaseModel.metadata.create_all(bind=engine)
            logger.info("Tables created successfully.")
        except Exception as e:
            logger.exception(
                "Failed to create tables. Error details: " + str(e)
            )

        logger.info("Database initialization complete.")
    else:
        logger.info("Database initialization skipped.")


def get_db_connection_status():
    """
    Check the database connection status.

    Returns:
        bool: True if the connection to the database is successful, False
        otherwise.

    Note:
        Logs a success or failure message based on the connection status.
    """
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        logger.info("Database connection is successful.")
        return True
    except Exception as e:
        logger.exception(
            "Database connection failed. Error details: " + str(e)
        )
        return False
