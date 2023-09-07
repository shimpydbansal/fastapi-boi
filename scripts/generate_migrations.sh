#!/bin/sh -e
set -x

# Activate the virtual environment
source .venv/bin/activate

alembic revision --autogenerate -m "Auto-generated migration"
alembic upgrade head
