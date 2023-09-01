#!/bin/sh -e
set -x

source venv/bin/activate

# Remove unused imports and variables
autoflake \
  --remove-all-unused-imports \
  --recursive \
  --remove-unused-variables \
  --in-place src \
  --exclude=__init__.py,venv

# Sort imports
isort --force-single-line-imports --line-length 79 src

# Reformat code using Black
black -l 79 src --exclude=venv

# Format code according to PEP 8
autopep8 --in-place --aggressive --aggressive --recursive src --exclude=venv
