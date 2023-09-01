"""User update schema."""
from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict

from module.user.schemas import UserSchema


class Config(ConfigDict):
    """Config defines the configuration for the BaseSchema class."""

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
    this defines the return attributes as a response when a user is updated.

    Attributes:
        id (UUID): The unique identifier for this user.
        updated_at (datetime): The date and time when this user was created.
        updated_by (Optional[UUID]): The unique identifier of the user who
        updated this user.
    """

    id: UUID
    updated_at: datetime
