#!/bin/sh -e
set -x

# Activate the virtual environment
source .venv/bin/activate

# Remove unused imports and variables
autoflake \
  --remove-all-unused-imports \
  --recursive \
  --remove-unused-variables \
  --in-place src \
  --exclude=__init__.py,.venv

# Sort imports
isort --force-single-line-imports --line-length 79 src

# Reformat code using Black
black -l 79 src --exclude=.venv,alembic/versions/*.py

# Format code according to PEP 8
autopep8 --in-place --aggressive --aggressive --recursive src --exclude=.venv
