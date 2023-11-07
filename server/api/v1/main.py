#!/usr/bin/env python
import uvicorn
from fastapi import FastAPI

from common.models import storage
from constants.config import settings

app = FastAPI()


@app.get('/')
async def root():
    return {'message': f'Hello from {storage}'}

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )