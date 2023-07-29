from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from common.base_service import BaseService
from modules.user.model import UserModel as User
from modules.user.schemas import UserCreateRequest
from modules.user.schemas import UserCreateResponse
from modules.user.schemas import UserSchema
from modules.user.schemas import UserUpdateRequest
from modules.user.schemas import UserUpdateResponse


class UserService(BaseService[User, UserCreateRequest, UserUpdateRequest]):
    def create_with_user(
        self, db: Session, *, obj_in: UserCreateRequest, user_id: str
    ) -> UserCreateResponse:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_session(
        self, db: Session, *, session_id: str, skip: int = 0, limit: int = 100
    ) -> List[UserSchema]:
        return (
            db.query(self.model)
            .filter(User.session_id == session_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


user = UserService(User)
