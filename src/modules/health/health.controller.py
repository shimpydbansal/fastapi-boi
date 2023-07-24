# from typing import List
from app.infrastructure import schemas
from app.infrastructure.database import SessionLocal
from app.infrastructure.repositories import health as health_repository
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# from app.infrastructure import models

router = APIRouter(
    prefix="/health",
    tags=["health"],
)


def get_db():
    """
    Dependency to get a database session for each request
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=schemas.HealthCheckResult)
def health(db: Session = Depends(get_db)):
    """
    Health check endpoint
    """
    return health_repository.health(db)
