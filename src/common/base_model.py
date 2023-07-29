"""
This module defines a SQLAlchemy base model class, from which other SQLAlchemy model
classes can inherit.

Imported modules used:
- typing: For type hints.
- sqlalchemy: For ORM (Object-Relational Mapping) functionality.
- sqlalchemy.dialects.postgresql: For PostgreSQL specific types.
- sqlalchemy.ext.declarative: For declarative base class.

This module contains the following classes:
    * BaseModel - A base model class that provides common attributes and methods for
    all other SQLAlchemy model classes.
"""

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative import declared_attr


@as_declarative()
class BaseModel:
    """
    Base Model for SQLAlchemy models.

    Attributes:
    id (UUID): A column of UUID type that serves as the primary key.
    created_at (DateTime): A column that stores the date and time of the record's
    creation.
    created_by (UUID): A column that stores the UUID of the user who created the
    record.
    updated_at (DateTime): A column that stores the date and time of the last update to
    the record.
    updated_by (UUID): A column that stores the UUID of the user who last updated the
    record.
    __name__ (str): The name of the SQLAlchemy model class.
    """

    id: Column(UUID, primary_key=True, index=True)
    created_at: Column(DateTime)
    created_by: Column(UUID)
    updated_at: Column(DateTime)
    updated_by: Column(UUID)
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        """
        Generate the __tablename__ attribute automatically based on the model's
        class name.

        Returns:
        str: The name of the table in lowercase.
        """

        return cls.__name__.lower()
