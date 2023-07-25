#!/bin/sh -e
set -x

poetry run pytest --cov=src --cov-report=term-missing --cov-fail-under=80 src "${@}"
