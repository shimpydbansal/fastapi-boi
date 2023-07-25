#!/bin/sh -e
set -x

# Check code formatting with black
poetry run black --check src || exit 1

# Check code formatting with flake8
poetry run flake8 src || exit 1
