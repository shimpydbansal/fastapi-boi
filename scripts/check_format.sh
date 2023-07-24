#!/bin/sh
set -e

# Check code formatting with black
black --check src || exit 1

# Check code formatting with flake8
flake8 src || exit 1
