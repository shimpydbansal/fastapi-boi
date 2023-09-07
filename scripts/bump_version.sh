#!/bin/sh -e
set -x

# Get the last commit message
commit_message=$(git log -1 --pretty=%B)

# Activate the virtual environment
source .venv/bin/activate

# Determine the version bump based on the commit message
if echo "$commit_message" | grep -q "^BREAKING CHANGE:"; then
    bump2version major
elif echo "$commit_message" | grep -q "^feature:"; then
    bump2version minor
elif echo "$commit_message" | grep -q "^fix:"; then
    bump2version patch
else
    echo "No version bump due to commit message format"
    exit 0  # If you want to fail the build in this case, replace with exit 1
fi
