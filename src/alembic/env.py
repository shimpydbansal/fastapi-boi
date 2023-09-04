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
from alembic.autogenerate import produce_migrations
from src.common import BaseModel

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

current_schema = os.getenv("DB_SCHEMA", "project1_schema")

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def check_and_delete_empty_migration():
    """
    Check the latest migration file and delete if it's found to be empty.

    This function identifies the most recently generated migration file
    within the 'versions' directory. If the migration file does not contain
    any operations or SQLAlchemy commands (i.e., lacks "op." and "sa."),
    the file is considered empty and is deleted.
    """
    # Path to the versions directory
    versions_path = os.path.join(current_dir, "versions")

    # List all .py files (excluding __init__.py) and sort them by modification
    # time
    all_migrations = sorted(
        [
            f
            for f in os.listdir(versions_path)
            if f.endswith(".py") and f != "__init__.py"
        ],
        key=lambda f: os.path.getmtime(os.path.join(versions_path, f)),
        reverse=True,  # From latest to earliest
    )

    if not all_migrations:
        return

    latest_migration_path = os.path.join(versions_path, all_migrations[0])

    print(f"Checking {latest_migration_path}")
    with open(latest_migration_path, "r") as file:
        content = file.read()
        if "op." not in content and "sa." not in content:
            os.remove(latest_migration_path)


def get_url():
    """Return the database URL that is based on the environment variables.

    The function reads the following environment variables:
    - DB_USER: The username for the database connection. Defaults 'project1'.
    - DB_PASSWORD: The password for the database connection.
        Defaults 'project1'.
    - DB_HOST: The hostname for the database connection. Defaults 'localhost'.
    - DB_PORT: The port number for the database connection. Defaults '5432'.
    - DB_NAME: The name of the database to connect to. Defaults 'project1'.

    Returns:
    A string representing the database URL in the format
    'postgresql://user:password@host:port/database'.
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
        include_schemas=True,
    )

    with context.begin_transaction():
        context.run_migrations()

    # check_and_delete_empty_migration()


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
            include_schemas=True,
        )

        # Get the Alembic context
        alembic_context = context.get_context()

        # Generate the diff between metadata and database
        # migration_context = Operations(alembic_context)
        diff = produce_migrations(alembic_context, target_metadata)

        # Check if the diff has any operations (changes)
        if not diff.upgrade_ops.is_empty():
            # If no operations are found, raise an exception to prevent
            # the creation of the migration file
            print("No changes detected. No migration file generated.")
            sys.exit(0)

        with context.begin_transaction():
            context.run_migrations()

        # check_and_delete_empty_migration()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
