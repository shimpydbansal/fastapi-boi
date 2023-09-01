"""Module for all the routes of the application."""
from fastapi import APIRouter

from module.health.health_controller import router as health_router
from module.user.user_controller import router as user_router

# import os
# import sys

# # Set the current directory path
# current_dir = os.path.dirname(os.path.abspath(__file__))
# # Get the parent directory path
# parent_dir = os.path.dirname(current_dir)
# print(parent_dir)
# sys.path.append(parent_dir)


router = APIRouter()
router.include_router(health_router)
router.include_router(user_router)
