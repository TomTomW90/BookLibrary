from abc import ABC, abstractmethod

from classes.UI_basic import UIBasic
from classes.book import Book


class UIEmplyee(ABC, UIBasic):

    def add_book_to_library(self, book: Book) -> None:  # add_book interface class should be added
        self._lib.books[book.get_isbn()] = book

    @abstractmethod
    def add_user(self):  # add_user interface class should be added
        pass

    @abstractmethod
    def edit_user(self):
        pass

    @abstractmethod
    def remove_user(self):
        pass
