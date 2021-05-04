from typing import Dict

from classes.book import Book
from classes.user_admin import Admin
from classes.user_librarian import Librarian
from classes.user_student import Student


class LibraryData:

    def __init__(self):
        self._books = {}
        self._students = {}
        self._librarians = {}
        self._admins = {}

    @property
    def books(self) -> Dict[int, Book]:
        return self._books

    @property
    def students(self) -> Dict[int, Student]:
        return self._students

    @property
    def librarians(self) -> Dict[str, Librarian]:
        return self._librarians

    @property
    def admins(self) -> Dict[str, Admin]:
        return self._librarians
