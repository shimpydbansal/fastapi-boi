#!/bin/sh -e
set -x

# Activate the virtual environment
source .venv/bin/activate

mypy src
black src --check
isort --check-only app
flake8
