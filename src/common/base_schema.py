"""This module defines a base schema class.

from which other schema classes can inherit.

It includes common attributes like id, creation and update timestamps,
and user identifiers for creation and updates.
"""


import uuid
from datetime import datetime
from typing import Any
from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict


class Config(ConfigDict):
    """Configuration class for Pydantic models."""

    arbitrary_types_allowed = True


class BaseSchema(BaseModel):
    """
    Define the common attributes to be used by other models.

    Attributes:
        id (Optional[UUID]): The unique identifier for this object.
        created_at (Optional[datetime]): The date and time when this object
        was created.
        created_by (Optional[UUID]): The unique identifier of the user who
        created this object.
        updated_at (Optional[datetime]): The date and time when this object
        was last updated.
        updated_by (Optional[UUID]): The unique identifier of the user who last
        updated this object.
    """

    id: UUID
    created_at: Optional[datetime] = None
    created_by: Optional[UUID] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[UUID] = None

    def __init__(self, **data: Any):
        """
        Initialize a new instance of the BaseSchema class.

        If an 'id' key is present in the data, the 'updated_at' attribute
        will be set to the current time.
        If an 'id' key is not present, it will be generated as a new UUID,
        and the 'created_at' attribute will be set to the current time.

        Args:
            data (Any): A dictionary containing the attributes to
            be set on the instance.
        """
        if "id" in data:
            data["updated_at"] = datetime.utcnow()
        if "id" not in data:
            data["id"] = uuid.uuid4()
        if "created_at" not in data:
            data["created_at"] = datetime.utcnow()

        super().__init__(**data)

    class Config:
        """
        Internal configuration class for the BaseSchema.

        Attributes:
            from_attributes (bool): Flag to control whether
            Pydantic builds the model from attributes.
        """

        from_attributes = True
