#!/bin/sh -e
set -x

source venv/bin/activate

alembic upgrade head
