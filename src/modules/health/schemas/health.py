from typing import Any
from typing import Optional
from xmlrpc.client import boolean

from pydantic import BaseModel
from pydantic import ConfigDict


class Config(ConfigDict):
    arbitrary_types_allowed = True


# Shared properties
class HealthResponse(BaseModel):
    """
    BaseSchema defines the common attributes to be used by other models.

    Attributes:
        id (Optional[UUID]): The unique identifier for this object.
        created_at (Optional[datetime]): The date and time when this object was created.
        created_by (Optional[UUID]): The unique identifier of the user who created this object.
        updated_at (Optional[datetime]): The date and time when this object was last updated.
        updated_by (Optional[UUID]): The unique identifier of the user who last updated this object.
    """

    database: bool = False
    message: str = "Ok!"
