from sqlalchemy.orm import Session

# from sqlalchemy.orm import sessionmaker

# import crud
# import schemas
# from core.config import settings
import os
import sys

from db import Base  # noqa: F401
from db.session import engine

# from crud import crud_message
# from models import Message
# from schemas import MessageCreate


current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


# import uuid

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    Base.metadata.create_all(bind=engine)

    # Create a session
    # Session = sessionmaker(bind=engine)
    # session = Session()

    # message = crud_message.message.get_by_email(db)
    # if not message:
    # message_in = MessageCreate(
    #     id=uuid.uuid4(),
    #     question="Hi",
    #     answer="Bye",
    #     user_id="jhjhdkjahkjdhjka",
    # )
    # message = crud_message.message.create(db, obj_in=message_in)  # noqa: F841
    # print(message)
