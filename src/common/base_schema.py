import uuid
from datetime import datetime
from typing import Any
from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict


class Config(ConfigDict):
    arbitrary_types_allowed = True


# Shared properties
class BaseSchema(BaseModel):
    """
    BaseSchema defines the common attributes to be used by other models.

    Attributes:
        id (Optional[UUID]): The unique identifier for this object.
        created_at (Optional[datetime]): The date and time when this object was created.
        created_by (Optional[UUID]): The unique identifier of the user who created this object.
        updated_at (Optional[datetime]): The date and time when this object was last updated.
        updated_by (Optional[UUID]): The unique identifier of the user who last updated this object.
    """

    id: UUID
    created_at: Optional[datetime] = None
    created_by: Optional[UUID] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[UUID] = None

    def __init__(self, **data: Any):
        if "id" in data:
            data["updated_at"] = datetime.utcnow()
        if "id" not in data:
            data["id"] = uuid.uuid4()
        if "created_at" not in data:
            data["created_at"] = datetime.utcnow()

        super().__init__(**data)

    class Config:
        from_attributes = True
