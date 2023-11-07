#!/usr/bin/env python
''' Initialize the models package '''
from os import getenv
from fastapi import FastAPI


app = FastAPI()
storage_t = getenv('STORAGE_TYPE')
if storage_t == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage(app)

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()