from typing import Dict

from classes.book import Book


class LibraryData:

    def __init__(self):
        self._books = {}
        self._users = {}

    @property
    def books(self) -> Dict[int, Book]:
        return self._books

    @property
    def users(self) -> dict:
        return self._users
