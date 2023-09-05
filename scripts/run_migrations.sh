#!/bin/sh -e
set -x

# Set (or export) necessary environment variables, if they aren't set elsewhere
# Example:
# export POSTGRES_SCHEMA=your_schema
# export POSTGRES_USER=your_user
# export POSTGRES_DB=your_database

# Create the SQL script using the POSTGRES_SCHEMA environment variable
echo "CREATE SCHEMA IF NOT EXISTS $POSTGRES_SCHEMA;" > /tmp/init.sql
echo "ALTER USER $POSTGRES_USER SET search_path TO $POSTGRES_SCHEMA;" >> /tmp/init.sql

# Run the script with psql to create the schema and set the search path
psql -h localhost -p 5432 -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" < /tmp/init.sql

# Activate the virtual environment
source .venv/bin/activate

# Run migrations
alembic upgrade head
