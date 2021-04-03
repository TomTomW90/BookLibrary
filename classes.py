from library_exceptions import EmptyLibraryError, NoAvailBook, NoBookFound


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

    def get_isbn(self) -> int:
        return self._isbn

    def get_title(self) -> str:
        return self._title

    def get_author_name(self) -> str:
        return self._author_name

    @property
    def manage_availability(self) -> bool:
        return self._is_available

    @manage_availability.setter
    def manage_availability(self, status: bool) -> None:
        self._is_available = self.validate_is_available(status)

    def __str__(self) -> str:
        return f"{self._title} / {self._author_name} ; ISBN: {self._isbn}"

    def __repr__(self):
        return f'Book(isbn={self._isbn}, title={self._title}, author_name={self._author_name}, is_available={self._is_available})'


class LibrarySystem:

    def __init__(self):
        self._books = {}

    def list_all_isbns_in_the_library(self) -> list:
        return list(self._books.keys())

    def add_book_to_library(self, book: Book) -> None:
        self._books[book.get_isbn()] = book

    def rent(self, isbn: int) -> None:
        if isbn == "":
            raise ValueError('ISBN argument is not given!')

        elif not isinstance(isbn, int):
            raise ValueError('Given ISBN is incorrect type!')

        elif isbn not in self.list_all_isbns_in_the_library():
            raise KeyError('Given ISBN does not exist in the library!')

        else:
            self._books[isbn].manage_availability = False

    def give_back(self, isbn: int) -> None:
        if isbn == "":
            raise ValueError('ISBN argument is not given!')

        elif not isinstance(isbn, int):
            raise ValueError('Given ISBN is incorrect type!')

        elif isbn not in self.list_all_isbns_in_the_library():
            raise KeyError('Given ISBN does not exist in the library!')

        else:
            self._books[isbn].manage_availability = True

    def list_available_books(self) -> list:
        if not self._books:
            raise EmptyLibraryError

        available_books = [book for book in self._books.values() if book.manage_availability]

        if not available_books:
            raise NoAvailBook

        return available_books

    def search_by_isbn(self, isbn_num: int) -> Book:
        try:
            isbn_num = Book.validate_isbn(isbn_num)
            return self._books[isbn_num]
        except KeyError:
            return 'Given ISBN does not exist.'

    def search_by_title(self, title_input: str, available_only: bool = True) -> list:
        title_input = Book.validate_title(title_input)
        books_list_with_title_input = [book for book in self._books.values() if
                                       title_input.lower() == book.get_title().lower()]
        if available_only:
            books_list_with_title_input = [book for book in books_list_with_title_input if book.manage_availability]

        if not books_list_with_title_input:
            raise NoBookFound

        return books_list_with_title_input

    def search_by_author(self, author_input: str, available_only: bool = True) -> list:
        author_input = Book.validate_author_name(author_input)
        books_list_with_author_input = [book for book in self._books.values() if
                                        author_input.lower() == book.get_author_name().lower()]
        if available_only:
            books_list_with_author_input = [book for book in books_list_with_author_input if book.manage_availability]

        if not books_list_with_author_input:
            raise NoBookFound

        return books_list_with_author_input

    def search_by_keyword(self, keyword: str, available_only: bool = True) -> list:
        if not isinstance(keyword, str) or keyword == '':
            raise ValueError("The keyword is not a string or is empty!")

        books_with_keyword = []
        for book in self._books.values():
            if (keyword.lower() in book.get_title().lower()) or (keyword.lower() in book.get_author_name().lower()):
                books_with_keyword.append(book)
        if available_only:
            books_with_keyword = [book for book in books_with_keyword if book.manage_availability]

        if not books_with_keyword:
            raise NoBookFound

        return books_with_keyword
