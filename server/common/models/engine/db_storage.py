#!/usr/bin/env python
''' DBStorage module '''
from fastapi import FastAPI


class DBStorage:
    ''' DBStorage class '''
    __app: FastAPI | None = None

    def __init__(self, app: FastAPI):
        ''' Initialize a DBStorage class '''
        self.__app = app
        self.start()
    
    def start():
        ''' Start a connection to the Database '''
        pass
    
    def close():
        ''' Close a connection to the Database '''
        pass