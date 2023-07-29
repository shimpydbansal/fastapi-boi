#!/bin/sh -e
set -x

isort --force-single-line-imports --line-length 80 src
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src --exclude=__init__.py
black -l 80 src
isort --line-length 80 src
