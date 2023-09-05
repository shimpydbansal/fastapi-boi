#!/bin/sh -e
set -x

export PYTHONPATH=$(pwd)/src:$PYTHONPATH
export ENVIRONMENT=test
poetry run pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=10 src "${@}"
