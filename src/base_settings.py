from pydantic_settings import BaseSettings
from typing import Optional


class PostgresSettings(BaseSettings):
    user: str = 'user'
    password: str = 'password'
    db: str = 'fastapi_shop'
    host: str = 'db'
    port: int = 5432
    url: str = 'postgresql+asyncpg://user:password@db:5432/fastapi_shop'
    api_key: Optional[str] = None


class ProjectSettings(BaseSettings):
    api_key: Optional[str] = None
    debug: Optional[bool] = True
    api_logger_format: Optional[str] = '%(levelname)s: %(asctime)s - %(message)s'

    postgres: PostgresSettings = PostgresSettings()

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


base_settings = ProjectSettings()
