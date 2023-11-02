#!/usr/bin/env python3
''' Base model module '''
from uuid import uuid4
from datetime import datetime
from pydantic import BaseModel, Field


TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S'
DATA = {}


class Base(BaseModel):
    ''' Base model class '''
    id: str = Field(default_factory=uuid4, alias='_id')

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


