
from copy import copy


class Book:

    def __init__(self, isbn: int, title: str, author_name: str, is_available: bool = True):
        self._isbn = self.validate_isbn(isbn)
        self._title = self.validate_title(title)
        self._author_name = self.validate_author_name(author_name)
        self._is_available = self.validate_is_available(is_available)

    def __str__(self) -> str:
        return f"{self._title} / {self._author_name} ; ISBN: {self._isbn}"

    def __repr__(self):
        return f'Book(isbn={self._isbn}, title={self._title}, author_name={self._author_name}, is_available={self._is_available})'

    @staticmethod
    def validate_isbn(isbn: int) -> int:
        if not isinstance(isbn, int) or isbn == "":
            raise ValueError("ISBN is wrong type or empty!")
        return isbn

    @staticmethod
    def validate_title(title: str) -> str:
        if not isinstance(title, str) or title == "":
            raise ValueError("Title is not a string or empty!")
        return title

    @staticmethod
    def validate_author_name(author_name: str) -> str:
        if not isinstance(author_name, str) or author_name == "":
            raise ValueError("Author is not a string or empty!")
        return author_name

    @staticmethod
    def validate_is_available(is_available: bool) -> bool:
        if not isinstance(is_available, bool):
            raise ValueError("Availability status is not 'True' or 'False'!")
        return is_available

    @property
    def manage_isbn(self) -> int:
        return self._isbn

    @manage_isbn.setter
    def manage_isbn(self, isbn: int) -> None:
        self._isbn = self.validate_isbn(isbn)

    @property
    def manage_title(self) -> str:
        return self._title

    @manage_title.setter
    def manage_title(self, title: int) -> None:
        self._title = self.validate_title(title)

    @property
    def manage_author_name(self) -> str:
        return self._author_name

    @manage_author_name.setter
    def manage_author_name(self, author_name: int) -> None:
        self._author_name = self.validate_author_name(author_name)

    @property
    def manage_availability(self) -> bool:
        return self._is_available

    @manage_availability.setter
    def manage_availability(self, status: bool) -> None:
        self._is_available = self.validate_is_available(status)

    def create_clone(self):
        return copy(self)


class BookPrototype:
    _prototype = Book(123456, 'Prototype_of_book', 'Developer', True)

    @staticmethod
    def create_new_book(isbn: int, title: str, author: str):
        books_clone = BookPrototype._prototype.create_clone()
        books_clone.manage_isbn = isbn
        books_clone.manage_title = title
        books_clone.manage_author_name = author
        return books_clone
