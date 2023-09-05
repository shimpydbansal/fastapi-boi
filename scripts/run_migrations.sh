#!/bin/sh -e
set -x

# Activate the virtual environment
source .venv/bin/activate

# Run migrations
alembic upgrade head
