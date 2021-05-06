from typing import Dict

from classes.book import Book
from classes.user_admin import Admin
from classes.user_librarian import Librarian
from classes.user_student import Student


class LibraryData:

    def __init__(self):
        self._books = {}
        self._users = {}
        self._user_types = {
            'Admin': Admin,
            'Librarian': Librarian,
            'Student': Student,
        }

    @property
    def books(self) -> Dict[int, Book]:
        return self._books

    @property
    def users(self) -> dict:
        return self._users

    @property
    def users_types(self) -> list:
        return self._user_types
