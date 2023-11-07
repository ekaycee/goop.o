from pydantic import BaseSettings
from os import getenv


class CommonSettings(BaseSettings):
    APP_NAME: str = 'GOOPO'
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = getenv('API_HOST') | '0.0.0.0'
    PORT: int = getenv('API_PORT') | 8000


class DatabaseSettings(BaseSettings):
    DB_HOST: str = getenv('DB_HOST') | '127.0.0.1'
    DB_PORT: int = getenv('DB_PORT') | 27017
    DB_NAME: str = getenv('DB_NAME') | 'goopo'


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()