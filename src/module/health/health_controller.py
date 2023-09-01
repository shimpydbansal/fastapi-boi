"""HealthController module."""
# from typing import List
# from app.infrastructure import schemas
# from app.infrastructure.database import SessionLocal
# from app.infrastructure.repositories import health as health_repository
from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from config import get_db_connection_status
from module.health.schemas import HealthResponse

router = APIRouter(tags=["Health"])


@router.get("/", response_model=HealthResponse)
@router.get("/health")
def health(db: Session = Depends(get_db_connection_status)) -> Any:
    """Health check endpoint."""
    db_status = get_db_connection_status()
    return {"database": db_status, "message": "Ok!"}
