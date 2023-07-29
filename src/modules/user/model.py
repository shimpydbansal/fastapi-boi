from os import name

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID

from common import BaseModel


class UserModel(BaseModel):
    __tablename__ = "user"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    created_by = Column(UUID)
    updated_at = Column(DateTime)
    updated_by = Column(UUID)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}', is_active='{self.is_active}', created_at='{self.created_at}', created_by='{self.created_by}', updated_at='{self.updated_at}', updated_by='{self.updated_by}')>"
