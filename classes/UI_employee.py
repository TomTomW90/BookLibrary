from abc import ABC, abstractmethod

from classes.UI_basic import UIBasic
from classes.UM_Builder import StudentBuilder, UserDirector
from classes.book import BookCreator


class UIEmployee(ABC, UIBasic):

    def add_book_to_library(self, isbn: int, title: str, author: str) -> None:
        new_book = BookCreator.create_new_book(isbn, title, author)
        self.lib.books[new_book.manage_isbn] = new_book

    def add_student_user(self, first_name: str, last_name: str, login: str, pesel: int):
        director = UserDirector()
        director.builder = StudentBuilder()
        new_student = director.create_new_student(first_name, last_name, login, pesel)
        self.lib.users[new_student.user_id] = new_student

    @abstractmethod
    def remove_user(self, user_id) -> None:
        pass
