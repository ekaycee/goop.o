#!/usr/bin/env python3
''' Base model module '''
from uuid import uuid4
from datetime import datetime
from pydantic import BaseModel, Field
from inflect import engine


TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S'
DATA = {}
p = engine()


class Base(BaseModel):
    ''' Base model class '''
    id: str = Field(default_factory=uuid4, alias='_id')
    __name__: str
    created_at: str = Field(...)
    updated_at: str = Field(...)

    def __init__(self, *args: list, **kwargs: dict):
        ''' Initialize a Base instance '''
        s_class = str(self.__class__.__name__)
        if DATA.get(s_class) is None:
            DATA[s_class] = {}

        self.id = kwargs.get('id', str(uuid4()))
        if kwargs.get('created_at') is not None:
            self.created_at = datetime.strptime(kwargs.get('created_at'),
                                                TIMESTAMP_FORMAT)
        else:
            self.created_at = datetime.utcnow()
        if kwargs.get('updated_at') is not None:
            self.updated_at = datetime.strptime(kwargs.get('updated_at'),
                                                TIMESTAMP_FORMAT)
        else:
            self.updated_at = datetime.utcnow()

    def __colname__(cls) -> str:    
        ''' Generate collection name automatically '''
        return p.plural(cls.__name__.lower())

    class Config:
        ''' Configure the Base model class '''
        populate_by_name = True


