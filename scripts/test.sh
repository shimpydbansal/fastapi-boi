#!/bin/sh -e
set -x

export ENVIRONMENT=test
poetry run pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=75 src "${@}"
