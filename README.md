# project-1

This is a description of my project. It does X, Y, and Z.

## Project Structure

The project has the following structure:

- `src/`: This is where the source code of the application lives.
    - `config/`: Configuration files.
    - `utils/`: Utility scripts and functions.
    - `modules/`: Each module of the application has its own directory in this folder. Each module directory contains:
        - `module.controller.py`: Defines the routes for this module.
        - `module.model.py`: Defines the data model for this module.
        - `module.service.py`: Contains business logic related to this module.
        - `module.repository.py`: Contains functions for interacting with the database.
- `tests/`: Test cases for the application.
- `pyproject.toml`: Lists the project's dependencies. Managed by Poetry.

## Setting Up for Development

1. Install Poetry: `pip install poetry`
2. Install the project's dependencies: `poetry install`
3. Run the application: `python main.py`

## Running Tests

Tests are written using pytest. To run them, use the command `pytest`.

## Building Documentation

Documentation is generated using Sphinx. To build the documentation, navigate to the `docs/` directory and run `make html`. The documentation will be built in `docs/_build/html`.
