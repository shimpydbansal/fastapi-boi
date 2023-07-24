#!/bin/sh -e
set -x

# Generate the documentation
sphinx-apidoc -o docs/build src/

# Generate the markdown files from rst
sphinx-build -b markdown -a -E docs/source docs/build

# Copy the generated markdown files to the documentation folder
cp docs/build/*.md documentation/docs/
cp src/**/*.md documentation/docs/
cp README.md documentation/docs/
