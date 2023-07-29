# from typing import Optional, Any

from pydantic import EmailStr

from common.base_schema import BaseSchema


# Properties to receive on item update
class UserSchema(BaseSchema):
    name: str
    email: EmailStr
