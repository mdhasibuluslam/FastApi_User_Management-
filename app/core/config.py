from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # ==========================
    # APP
    # ==========================

    APP_NAME: str

    APP_VERSION: str

    ENVIRONMENT: str

    DEBUG: bool

    # ==========================
    # DATABASE
    # ==========================

    DATABASE_URL: str

    # ==========================
    # JWT
    # ==========================

    SECRET_KEY: str

    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    REFRESH_TOKEN_EXPIRE_DAYS: int

    # ==========================
    # REDIS
    # ==========================

    REDIS_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


@lru_cache
def get_settings():

    return Settings()


settings = get_settings()

