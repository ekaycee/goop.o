from uuid import uuid4
from pydantic import Field

from common.models.user import User


class Book:
    ''' Book model class '''
    id: str = Field(default_factory=uuid4, alias='_id')
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


class BookCategory:
    ''' BookCategory model class '''
    id: str = Field(default_factory=uuid4, alias='_id')
    name: str = Field(...)


class BookChapter:
    ''' BookChapter model class '''
    id: str = Field(default_factory=uuid4, alias='_id')
    title: str = Field(...)
    number: int = Field(...)
    content: str = Field(...)
    comments: list[BookChapterComment] = []


class BookChapterComment:
    ''' BookChapterComment model class '''
    id: str = Field(default_factory=uuid4, alias='_id')
    title: str = Field(...)
    comment: str = Field(...)
    creator: User = Field(...)


class BookReview:
    ''' BookReview model class '''
    id: str = Field(default_factory=uuid4, alias='_id')
    title: str = Field(...)
    rating: int = Field(...)
    content: str | None = None
    creator: User = Field(...)


