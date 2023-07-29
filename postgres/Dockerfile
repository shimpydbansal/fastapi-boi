FROM postgres:14.8-alpine

# Copy the shell script and change its permissions
COPY init.sh /docker-entrypoint-initdb.d/

# Make sure the shell script is executable
RUN chmod +x /docker-entrypoint-initdb.d/init.sh
