# Base image for building dependencies
FROM python:3.11 AS build

# Set working directory
WORKDIR /app

# Copy only the files needed for installing dependencies
COPY src/ /app/src/
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install --no-cache-dir poetry

# Configure poetry
RUN poetry config virtualenvs.create false --local

# Install project dependencies
RUN poetry install --no-dev

# Final image for running the application
FROM python:3.11 AS release

# Set working directory
WORKDIR /app

# Copy source code
COPY --from=build /app/src/ /app/src/

# Copy installed dependencies from the builder image
COPY --from=build /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=build /usr/local/bin/ /usr/local/bin/

# Set environment variables
ENV PYTHONPATH /app/src

# Expose port
EXPOSE 80

# Start the web service
CMD ["bash", "-c", "alembic upgrade head && uvicorn src.main:app --host 0.0.0.0 --port 80"]
