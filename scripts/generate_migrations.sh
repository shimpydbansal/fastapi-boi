#!/bin/sh -e
set -x

source venv/bin/activate

alembic revision --autogenerate -m "Auto-generated migration"
