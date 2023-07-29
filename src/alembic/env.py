"""
This module contains the database migration scripts for the project.

Functions:
- get_url(): Returns the database URL based on the environment variables.
- run_migrations_offline(): Runs the database migrations in offline mode.
- run_migrations_online(): Runs the database migrations in online mode.
"""

from __future__ import with_statement

import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy import text

from alembic import context
from common import BaseModel

# set parent directory path
# Get the current file's directory
current_dir = os.path.abspath(os.path.dirname(__file__))
# Get the parent directory path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

target_metadata = BaseModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_url():
    """Return the database URL that is based on the environment variables.

    The function reads the following environment variables:
    - DB_USER: The username for the database connection. Defaults to 'project1'.
    - DB_PASSWORD: The password for the database connection. Defaults to 'project1'.
    - DB_HOST: The hostname for the database connection. Defaults to 'localhost'.
    - DB_PORT: The port number for the database connection. Defaults to '5432'.
    - DB_NAME: The name of the database to connect to. Defaults to 'project1'.

    Returns:
    A string representing the database URL in the format 'postgresql://user:password@host:port/database'.
    """
    user = os.getenv("DB_USER", "project1")
    password = os.getenv("DB_PASSWORD", "project1")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    database = os.getenv("DB_NAME", "project1")

    return f"postgresql://{user}:{password}@{host}:{port}/{database}"


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    current_schema = os.getenv("DB_SCHEMA", "project1_schema")
    with connectable.connect() as connection:
        # set search path on the connection, which ensures that
        # PostgreSQL will emit all CREATE / ALTER / DROP statements
        # in terms of this schema by default
        connection.execute(text('set search_path to "%s"' % current_schema))
        # in SQLAlchemy v2+ the search path change needs to be committed
        connection.commit()

        # make use of non-supported SQLAlchemy attribute to ensure
        # the dialect reflects tables in terms of the current tenant name
        connection.dialect.default_schema_name = current_schema

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
