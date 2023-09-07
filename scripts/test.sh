#!/bin/sh -e
set -x

export PYTHONPATH=$(pwd)/src:$PYTHONPATH
export ENVIRONMENT=test

# Activate the virtual environment
source .venv/bin/activate

poetry run pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=75 src "${@}"
