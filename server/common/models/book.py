#!/usr/bin/env python
''' Book model module '''
from uuid import uuid4
from pydantic import Field

from common.models.base import Base
from common.models.user import User


class BookCategory(Base):
    ''' BookCategory model class '''
    name: str = Field(...)


class BookChapterComment(Base):
    ''' BookChapterComment model class '''
    title: str = Field(...)
    comment: str = Field(...)
    creator: User = Field(...)


class BookChapter(Base):
    ''' BookChapter model class '''
    title: str = Field(...)
    number: int = Field(...)
    content: str = Field(...)
    comments: list[BookChapterComment] = []


class BookReview(Base):
    ''' BookReview model class '''
    title: str = Field(...)
    rating: int = Field(...)
    content: str | None = None
    creator: User = Field(...)


class Book(Base):
    ''' Book model class '''
    title: str = Field(...)
    status: str = Field(...)
    author: User = Field(...)
    synopsis: str | None = None
    views: int | None = None
    rating: float | None = None
    categories: list[BookCategory] = []
    chapters: list[BookChapter] = []
    # for the future.. I'll be adding stuff like;
    # characters, cover_art,


