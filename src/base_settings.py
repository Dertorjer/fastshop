from typing import Optional

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class PostgresSettings(BaseModel):
    user: str = 'user'
    password: str = 'password'
    db: str = 'fastapi_shop'
    host: str = 'db'
    port: int = 5432
    url: str = 'postgresql+asyncpg://user:password@db:5432/fastapi_shop'
    api_key: str = "test_api_key"


class ProjectSettings(BaseSettings):
    api_key: str = "test_api_key"  # Встановлюємо значення за замовчуванням
    debug: Optional[bool] = True
    api_logger_format: Optional[str] = '%(levelname)s: %(asctime)s - %(message)s'

    postgres: PostgresSettings = PostgresSettings()

    model_config = SettingsConfigDict(
        env_nested_delimiter='__',
        frozen=True,
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )


base_settings = ProjectSettings()
