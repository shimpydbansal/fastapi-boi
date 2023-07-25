#!/bin/sh -e
set -x

bash scripts/test.sh --cov-report=html "${@}"
