from abc import ABC, abstractmethod

from classes.UI_basic import UIBasic
from classes.book import Book


class UIEmployee(ABC, UIBasic):

    def add_book_to_library(self, book: Book) -> None:  # add_book interface class should be added
        self._lib.books[book.get_isbn()] = book

    @abstractmethod
    def add_user(self, *args) -> None:
        pass

    @abstractmethod
    def edit_user(self, *args) -> None:
        pass

    @abstractmethod
    def remove_user(self, *args) -> None:
        pass
