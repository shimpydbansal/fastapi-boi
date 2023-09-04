"""This is user model."""

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String

from common.base_model import BaseModel


class UserModel(BaseModel):
    """This class defines a user model."""

    __tablename__ = "user"
    __table_args__ = {"schema": "project1_schema"}

    name = Column(String)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        """Return a string representation of this object."""
        return (
            f"<User(id={self.id}, name='{self.name}', email='{self.email}',"
            f"is_active='{self.is_active}', created_at='{self.created_at}', "
            f"created_by='{self.created_by}', updated_at='{self.updated_at}', "
            f"updated_by='{self.updated_by}')>"
        )
