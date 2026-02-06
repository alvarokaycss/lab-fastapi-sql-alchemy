from typing import ClassVar

from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações da aplicação.
    """

    API_V1_STR: str = "/api/v1"
    DB_URL: str
    DBBaseModel: ClassVar = declarative_base()
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    RELOAD: bool = True
    LOG_LEVEL: str = "INFO"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
