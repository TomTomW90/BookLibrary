from abc import ABC, abstractmethod

from classes.UI_basic import UIBasic
from classes.UM_Builder import StudentBuilder, UserDirector
from classes.book import Book


class UIEmployee(ABC, UIBasic):

    def add_book_to_library(self, book: Book) -> None:  # add_book interface class should be added
        self.lib.books[book.get_isbn()] = book

    def add_student_user(self, first_name: str, last_name: str, login: str, pesel: int):
        director = UserDirector()
        director.builder = StudentBuilder()
        new_student = director.create_new_student(first_name, last_name, login, pesel)
        self.lib.users[new_student.user_id] = new_student

    @abstractmethod
    def remove_user(self, user_id) -> None:
        pass
