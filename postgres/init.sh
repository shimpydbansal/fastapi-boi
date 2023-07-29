#!/bin/bash
set -e

# # Create the SQL script using the POSTGRES_SCHEMA environment variable
# echo "CREATE SCHEMA IF NOT EXISTS $POSTGRES_SCHEMA;" > /docker-entrypoint-initdb.d/init.sql
# echo "created file"
# echo "ALTER USER $POSTGRES_USER SET search_path TO $POSTGRES_SCHEMA;" >> /docker-entrypoint-initdb.d/init.sql
# echo "created file"


# Create the SQL script using the POSTGRES_SCHEMA environment variable
echo "CREATE SCHEMA IF NOT EXISTS $POSTGRES_SCHEMA;" > /tmp/init.sql
echo "ALTER USER $POSTGRES_USER SET search_path TO $POSTGRES_SCHEMA;" >> /tmp/init.sql

# Now use psql to run the script
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" < /tmp/init.sql
