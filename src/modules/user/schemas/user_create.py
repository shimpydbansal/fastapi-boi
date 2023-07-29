from datetime import datetime
from doctest import Example
from os import name
from typing import Any
from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import Field

from modules.user.schemas import UserSchema

# import modules.user.schemas.user_base as UserBaseSchema


class Config(ConfigDict):
    arbitrary_types_allowed = True


# Shared properties
class UserCreateRequest(UserSchema):
    """
    UserCreateRequest defines the attributes required to create a new user.

    Attributes:
        name (str): The name of the user.
        email (EmailStr): The email address of the user.
    """

    name: str
    email: EmailStr = Field(
        title="The description of the item", example="user@example.com"
    )


class UserCreateResponse(BaseModel):
    """
    UserCreateResponse defines the attributes to be returned as a response when a new user is created.

    Attributes:
        id (UUID): The unique identifier for this user.
        created_at (datetime): The date and time when this user was created.
        created_by (Optional[UUID]): The unique identifier of the user who created this user.
    """

    # Overriding the fields from BaseSchema to set them as required
    id: UUID
    created_at: datetime
