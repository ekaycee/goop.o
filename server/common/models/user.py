from uuid import uuid4
from typing import Optional
from pydantic import Field
from datetime import datetime


class User:
    ''' User model class '''
    id: str = Field(default_factory=uuid4, alias='_id')
    first_name: str = Field(...)
    middle_name: str = Field(...)
    last_name: str = Field(...)
    mobile: str = Field(...)
    email: str = Field(...)
    password_hash: str = Field(...)
    registered_at: datetime = datetime.now
    last_login: Optional[datetime]
    bio: Optional[str]
    dob: datetime
    profile: Optional[str]
