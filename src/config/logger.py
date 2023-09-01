"""Logger configuration for the project."""

import logging
import os

project_name = os.getenv("PROJECT_NAME", "fastapi-boilerplate")

# Create a custom logger
logger = logging.getLogger(project_name)

# Set level for logger
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(f"{project_name}.log")

# Set level for handlers
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.WARNING)

# Create formatters and add it to handlers
console_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
file_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
