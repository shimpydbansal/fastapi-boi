"""Environment variables configuration."""
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from pydantic import AnyHttpUrl
from pydantic import PostgresDsn
from pydantic import validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Environment variables configuration."""

    ENVIRONMENT: str = "development"
    PROJECT_NAME: str
    API_V1_STR: str = "/api/v1"
    # SERVER_NAME: str
    # SERVER_HOST: AnyHttpUrl
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", \
    # "http://localhost:8080", "http://localhost:3000"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(
        cls, v: Union[str, List[str]]
    ) -> Union[List[str], str]:
        """Transform the string of origins into a list of origins."""
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # SENTRY_DSN: Optional[HttpUrl] = None

    # @validator("SENTRY_DSN", pre=True)
    # def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
    #     if len(v) == 0:
    #         return None
    #     return v

    MAX_HISTORY_LENGTH: int = 5

    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_PORT: int
    DB_SCHEMA: str
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(
        cls, v: Optional[str], values: Dict[str, Any]
    ) -> Any:
        """Build the database connection string."""
        if isinstance(v, str):
            return v
        db_uri = PostgresDsn.build(
            scheme="postgresql",
            username=values.get("DB_USER"),
            password=values.get("DB_PASSWORD"),
            host=values.get("DB_HOST"),
            port=values.get("DB_PORT"),
            path=f"{values.get('DB_NAME')}",
        )

        return str(db_uri)

    class Config:
        """Configuration for environment variables."""

        def __init__(self):
            """Initialize the class."""

        case_sensitive = True
        env_file = ".env"
        check_fields = False


settings = Settings()
