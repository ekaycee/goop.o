#!/usr/bin/env python
''' Book controller module '''
from fastapi import Body, Request
from fastapi.encoders import jsonable_encoder

from common.models.book import Book


class BookController:
    ''' Book controller class '''

    def create_book(cls, req: Request, book: Book = Body(...)):
        ''' Create book method '''
        book = jsonable_encoder(book)

