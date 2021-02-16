class Book:

    def __init__(self, isbn: int, title: str, author_name: str, is_available: bool = True):
        self._isbn = self.validate_isbn(isbn)
        self._title = self.validate_title(title)
        self._author_name = self.validate_author_name(author_name)
        self._is_available = self.validate_is_available(is_available)

    @staticmethod
    def validate_isbn(isbn: int) -> int:
        if not isinstance(isbn, int) or isbn == "":
            raise ValueError("ISBN is wrong type or empty!")
        return isbn

    def validate_title(self, title: str) -> str:
        if not isinstance(title, str) or title == "":
            raise ValueError("Title is not a string or empty!")
        return title

    def validate_author_name(self, author_name: str) -> str:
        if not isinstance(author_name, str) or author_name == "":
            raise ValueError("Author is not a string or empty!")
        return author_name

    def validate_is_available(self, is_available: bool) -> bool:
        if not isinstance(is_available, bool):
            raise ValueError("Availability status is not 'True' or 'False'!")
        return is_available

    def get_isbn(self) -> int:
        return self._isbn

    def use_title(self) -> str:
        return self._title

    def use_author(self) -> str:
        return self._author_name

    @property
    def manage_availability(self) -> bool:
        return self._is_available

    @manage_availability.setter
    def manage_availability(self, status: bool) -> None:
        self._is_available = self.validate_is_available(status)

    def __repr__(self) -> str:
        return f"{self._title} / {self._author_name} ; ISBN: {self._isbn}"


class LibrarySystem:

    def __init__(self):
        self._books = {}

    def add_book_to_library(self, book: Book) -> None:
        self._books[book.get_isbn()] = book

    def rent(self, isbn: int) -> None:
        self._books[isbn].manage_availability(False)

    def give_back(self, isbn: int) -> None:
        self._books[isbn].manage_availability(True)

    def list_available_books(self) -> list:
        """Return list of Book class objects with parameter is_available==True."""

        available_books = [book for book in self._books.values() if book.manage_availability]
        return available_books

    def search_by_isbn(self, isbn_num: int) -> Book:
        """Return Book class """
        return self._books[isbn_num]

    def search_by_title(self, title_input: str) -> list:
        books_list_with_title_input = [book.use_title() for book in self._books.values() if title_input.lower() == book.use_title().lower()]
        return books_list_with_title_input

    def search_by_author(self, author_input: str) -> list:
        books_list_with_author_input = [book.use_title() for book in self._books.values() if author_input.lower() == book.use_author().lower()]
        return books_list_with_author_input

    def serach_by_keyword(self, keyword: str) -> list:
        books_with_keyword = []
        for book in self._books.values():
            if (keyword.lower() in book.use_title().lower()) or (keyword.lower() in book.use_author().lower()):
                books_with_keyword.append(book)
        return books_with_keyword
