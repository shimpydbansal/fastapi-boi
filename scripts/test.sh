#!/bin/sh -e
set -x

pytest --cov=src --cov-report=term-missing --cov-fail-under=80 src "${@}"
