"""UserController module."""
from typing import Annotated
from typing import List

# from api import deps
from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from config import get_db_session
from module.user.schemas import UserCreateRequest
from module.user.schemas import UserCreateResponse
from module.user.schemas import UserSchema
from module.user.schemas import UserUpdateRequest
from module.user.schemas import UserUpdateResponse
from module.user.user_service import user_service

router = APIRouter(tags=["User"])


@router.get("/users", response_model=List[UserSchema])
def read_messages(
    session_id: str,
    db: Session = Depends(get_db_session),
    skip: int = 0,
    limit: int = 100,
) -> List[UserSchema]:
    """Retrieve users."""
    users = user_service.get_multi_by_session(
        db=db, session_id=session_id, skip=skip, limit=limit
    )
    return users


@router.post("/users", response_model=UserCreateResponse)
def create_user(
    *, db: Session = Depends(get_db_session), message_in: UserCreateRequest
) -> UserCreateResponse:
    """Create new message."""
    user = user_service.create(db=db, obj_in=message_in)

    return user


@router.put("/users/{id}", response_model=UserUpdateResponse)
def update_message(
    *,
    db: Session = Depends(get_db_session),
    id: int,
    user: Annotated[UserUpdateRequest, Body(embed=True)],
    # current_user: models.User = Depends(deps.get_current_active_user),
) -> UserUpdateResponse:
    """Update an user."""
    user = user_service.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not UserService.user.is_superuser(current_user) and
    # (message.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    user = user_service.user.update(db=db, db_obj=user, obj_in=user)
    return user


# @router.get("/{id}", response_model=schemas.Message)
# def read_message(
#     *,
#     db: Session = Depends(get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Get message by ID.
#     """
#     message = UserService.message.get(db=db, id=id)
#     if not message:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not UserService.user.is_superuser(current_user)
#     and (message.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     return message


# @router.delete("/{id}", response_model=schemas.Message)
# def delete_message(
#     *,
#     db: Session = Depends(get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Delete an message.
#     """
#     message = UserService.message.get(db=db, id=id)
#     if not message:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not UserService.user.is_superuser(current_user)
#     and (message.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     message = UserService.message.remove(db=db, id=id)
#     return message
