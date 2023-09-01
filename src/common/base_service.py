"""
This module defines a base service class.

from which other service classes can inherit.

It includes common methods like get, create and update.
"""

from typing import Any
from typing import Dict
from typing import Generic
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import Union

from fastapi import HTTPException
from fastapi import status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from .base_model import BaseModel as Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    A generic service class that provides CRUD operations for a given model.

    Attributes:
        model (Type[ModelType]): The SQLAlchemy model class for
        which the CRUD operations are provided.
    """

    def __init__(self, model: Type[ModelType]):
        """
        Initialize the BaseService with the given model.

        Parameters:
            model (Type[ModelType]): A SQLAlchemy model class.
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        """
        Retrieve an object by its ID.

        Parameters:
            db (Session): The database session.
            id (Any): The ID of the object.

        Returns:
            Optional[ModelType]: The retrieved object if found, None otherwise.
        """
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        """
        Retrieve a list of objects with optional skipping and limiting.

        Parameters:
            db (Session): The database session.
            skip (int): Number of entries to skip before starting to fetch.
            limit (int): Maximum number of entries to fetch.

        Returns:
            List[ModelType]: The list of retrieved objects.
        """
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        """
        Create a new object in the database.

        Parameters:
            db (Session): The database session.
            obj_in (CreateSchemaType): The Pydantic model containing the
            object data to create.

        Returns:
            ModelType: The created object.

        Raises:
            HTTPException: If a database error or internal server error
            occurs.
        """
        try:
            obj_in_data = jsonable_encoder(obj_in)
            db_obj = self.model(**obj_in_data)  # type: ignore
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error",
            ) from e
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            ) from e

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        """
        Update an existing object in the database.

        Parameters:
            db (Session): The database session.
            db_obj (ModelType): The object to update.
            obj_in (Union[UpdateSchemaType, Dict[str, Any]]): The new data
            for the object.

        Returns:
            ModelType: The updated object.

        Note:
            If 'obj_in' is provided as a dictionary, it directly updates the
            object.
            If 'obj_in' is a Pydantic model, it first converts it to a
            dictionary.
        """
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        """
        Remove an object from the database by its ID.

        Parameters:
            db (Session): The database session.
            id (int): The ID of the object to remove.

        Returns:
            ModelType: The removed object.

        Note:
            The object is retrieved by ID and then deleted from the database.
        """
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
