from fastapi import APIRouter

from modules.health import health_router
from modules.user import user_router

router = APIRouter()
router.include_router(health_router)
router.include_router(user_router)
