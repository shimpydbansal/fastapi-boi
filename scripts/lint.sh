#!/bin/sh -e
set -x

mypy src
black src --check
isort --check-only app
flake8
