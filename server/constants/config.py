#!/usr/bin/env python
''' Settings config module '''
from pydantic_settings import BaseSettings
from os import getenv


class CommonSettings(BaseSettings):
    APP_NAME: str = 'GOOPO'
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = getenv('API_HOST') or '0.0.0.0'
    PORT: int = getenv('API_PORT') or 8000


class DatabaseSettings(BaseSettings):
    DB_HOST: str = getenv('DB_HOST') or '127.0.0.1'
    DB_PORT: int = getenv('DB_PORT') or 27017
    DB_NAME: str = getenv('DB_NAME') or 'goopo'


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()