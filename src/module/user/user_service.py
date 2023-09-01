"""User service module."""
from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from common.base_service import BaseService
from module.user.schemas import UserCreateRequest
from module.user.schemas import UserCreateResponse
from module.user.schemas import UserSchema
from module.user.schemas import UserUpdateRequest
from module.user.user_model import UserModel as User


class UserService(BaseService[User, UserCreateRequest, UserUpdateRequest]):
    """User service."""

    def create_with_user(
        self, db: Session, *, obj_in: UserCreateRequest, user_id: str
    ) -> UserCreateResponse:
        """Create a new user."""
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_session(
        self, db: Session, *, session_id: str, skip: int = 0, limit: int = 100
    ) -> List[UserSchema]:
        """Get multiple users by session."""
        return (
            db.query(self.model)
            .filter(User.session_id == session_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


user_service = UserService(User)
