"""this is main module."""


# from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import init_db
from config import logger
from config import settings

# from src.module.user import controller as user_controller
from module.routes import router

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


@app.on_event("startup")
def startup_event():
    """Execute the function when the application starts up."""
    # Create the database tables and set initial data
    if settings.ENVIRONMENT == "development":
        logger.info("Running init_db function.")
        init_db()
