from datetime import datetime
from typing import Any
from typing import Optional
from uuid import UUID

from pydantic import ConfigDict

from modules.user.schemas import UserSchema


class Config(ConfigDict):
    arbitrary_types_allowed = True


# Properties to receive on item update
class UserUpdateRequest(UserSchema):
    """
    UserUpdateRequest defines the attributes required to update a user.

    Attributes:
        name (str): The name of the user.
        email (EmailStr): The email address of the user.
    """

    id: UUID
    name: str


# Properties to receive on item update
class UserUpdateResponse(UserSchema):
    """
    UserUpdateResponse defines the attributes to be returned as a response when a user is updated.

    Attributes:
        id (UUID): The unique identifier for this user.
        updated_at (datetime): The date and time when this user was created.
        updated_by (Optional[UUID]): The unique identifier of the user who updated this user.
    """

    id: UUID
    updated_at: datetime
