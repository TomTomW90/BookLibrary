from classes.book import Book
from classes.lib_data import LibraryData
from classes.lib_exceptions import EmptyLibraryError, NoAvailBook, NoBookFound


class UIBasic:

    def __init__(self, lib: LibraryData):
        self._lib = lib

    @property
    def lib(self) -> LibraryData:
        return self._lib

    def list_all_isbns_in_the_library(self) -> list:
        return list(self.lib.books.keys())

    def rent(self, isbn: int) -> None:
        if isbn == "":
            raise ValueError('ISBN argument is not given!')
        elif not isinstance(isbn, int):
            raise ValueError('Given ISBN is incorrect type!')
        elif isbn not in self.list_all_isbns_in_the_library():
            raise KeyError('Given ISBN does not exist in the library!')
        else:
            self.lib.books[isbn].manage_availability = False

    def give_back(self, isbn: int) -> None:
        if isbn == "":
            raise ValueError('ISBN argument is not given!')
        elif not isinstance(isbn, int):
            raise ValueError('Given ISBN is incorrect type!')
        elif isbn not in self.list_all_isbns_in_the_library():
            raise KeyError('Given ISBN does not exist in the library!')
        else:
            self.lib.books[isbn].manage_availability = True

    def list_available_books(self) -> list:

        if not self.lib.books:
            raise EmptyLibraryError

        available_books = [book for book in self.lib.books.values() if book.manage_availability]

        if not available_books:
            raise NoAvailBook
        return available_books

    def search_by_isbn(self, isbn_num: int) -> Book:
        try:
            isbn_num = Book.validate_isbn(isbn_num)
            return self.lib.books[isbn_num]
        except KeyError:
            return 'Given ISBN does not exist.'

    def search_by_title(self, title_input: str, available_only: bool = True) -> list:
        title_input = Book.validate_title(title_input)
        books_list_with_title_input = [book for book in self.lib.books.values() if
                                       title_input.lower() == book.get_title().lower()]

        if available_only:
            books_list_with_title_input = [book for book in books_list_with_title_input if book.manage_availability]

        if not books_list_with_title_input:
            raise NoBookFound

        return books_list_with_title_input

    def search_by_author(self, author_input: str, available_only: bool = True) -> list:
        author_input = Book.validate_author_name(author_input)
        books_list_with_author_input = [book for book in self.lib.books.values() if
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
        for book in self.lib.books.values():
            if (keyword.lower() in book.get_title().lower()) or (keyword.lower() in book.get_author_name().lower()):
                books_with_keyword.append(book)
        if available_only:
            books_with_keyword = [book for book in books_with_keyword if book.manage_availability]

        if not books_with_keyword:
            raise NoBookFound

        return books_with_keyword
