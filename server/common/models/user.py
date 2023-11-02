#!/usr/bin/env python
''' User model module '''
from pydantic import Field
from datetime import datetime

from common.models.base import Base


class User(Base):
    ''' User model class '''
    first_name: str = Field(...)
    middle_name: str = Field(...)
    last_name: str = Field(...)
    username: str = Field(...)
    mobile: str = Field(...)
    email: str = Field(...)
    password_hash: str = Field(...)
    registered_at: datetime = datetime.now
    last_login: datetime | None = None
    bio: str | None = None
    dob: datetime = Field(...)
    profile: str | None = None
