#!/usr/bin/env python
''' Account model module '''
from uuid import uuid4
from pydantic import Field
from datetime import datetime

from .base import Base
from .user import User


class Account(Base):
    ''' Account model class '''
    name: str = Field(...)
    description: str = Field(...)
    is_active: bool = False
    plan_id: Field(default_factory=uuid4)
    current_subscription_ends: datetime | None = None
    users: list[User] | None = None