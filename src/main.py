# from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from src.modules.user import controller as user_controller
from app_module import router
from config import settings
from src.config import get_db_session
from src.config import init_db

# from sqlalchemy.orm import Session


app = FastAPI()

# Set all CORS enabled origins
origins = settings.BACKEND_CORS_ORIGINS

# Set CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/boilerplate/v1")

# @app.get("/health")
# async def health_check():
#     """
#     Health check endpoint
#     """
#     return {"message": "Ok!"}


# Dependency to get a database session for each request
# def get_db() -> Session:
#     try:
#         db = get_db_session()
#         yield db
#     finally:
#         db.close()


@app.on_event("startup")
def startup_event():
    # Create the database tables and set initial data
    try:
        db = get_db_session()
        init_db(db)
    finally:
        db.close()
