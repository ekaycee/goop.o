#!/usr/bin/env python
''' DBStorage module '''
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from constants.config import settings


class DBStorage:
    ''' DBStorage class '''
    __app: FastAPI | None = None

    def __init__(self, app: FastAPI):
        ''' Initialize a DBStorage class '''
        self.__app = app
    
    @__app.on_event('startup')
    async def open(self):
        ''' Start a connection to the Database '''
        self.__app.mongodb_client = AsyncIOMotorClient(settings.DB_HOST, settings.DB_PORT)
        self.__app.mongodb = self.__app.mongodb_client[settings.DB_NAME]

    async def reload(self):
        ''' Restart a connection to the Database '''
        self.close()
        self.open()
    
    @__app.on_event('shutdown')
    async def close(self):
        ''' Close a connection to the Database '''
        self.__app.mongodb_client.close()