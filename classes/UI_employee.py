from abc import ABC, abstractmethod

from classes.UI_basic import UIBasic
from classes.UM_creator import UMCreator
from classes.book import Book


class UIEmployee(ABC, UIBasic):

    def add_book_to_library(self, book: Book) -> None:  # add_book interface class should be added
        self._lib.books[book.get_isbn()] = book

    def add_student(self, students_id: int, students_first_name: str, students_last_name: str, students_login: str) -> None:
        self._lib.students[students_id] = UMCreator.create_student(students_id, students_first_name, students_last_name, students_login)

    @abstractmethod
    def edit_user(self, *args) -> None:
        pass

    @abstractmethod
    def remove_user(self, *args) -> None:
        pass
