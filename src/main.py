# from typing import Union

from fastapi import FastAPI

# from fastapi.middleware.cors import CORSMiddleware

# from sqlalchemy.orm import Session

# from api.api import router
# from db.session import SessionLocal
# from db.init_db import init_db

app = FastAPI()


#
# origins = ["http://localhost:3000", "http://localhost:3001"]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
# app.include_router(router)


@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"message": "Ok!"}


# Dependency to get a database session for each request
# def get_db() -> Session:
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# @app.on_event("startup")
# def startup_event():
#     # Create the database tables and set initial data
#     db = SessionLocal()
#     try:
#         init_db(db)
#     finally:
#         db.close()
