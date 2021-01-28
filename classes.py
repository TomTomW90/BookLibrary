class Book:

    def __init__(self, isbn: int, title: str, author_f_name: str, author_l_name: str, is_available=True):
        self.__isbn = isbn
        self._title = title
        self._author_f_name = author_f_name
        self._author_l_name = author_l_name
        self._is_available = is_available

    def __repr__(self) -> str:
        return f"{self._title} / {self._author_f_name} {self._author_l_name}; ISBN: {self.__isbn}"

    def get_isbn(self) -> int:
        return self.__isbn

    def get_title(self) -> str:
        return self._title

    def edit_title(self, title: str) -> None:
        self._title = title

    def edit_author(self, name: str, surname: str) -> None:
        self._author_f_name = name
        self._author_l_name = surname

    def get_author(self) -> str:
        return f'{self._author_l_name}, {self._author_f_name}'

    def get_availability(self) -> bool:
        return self._is_available

    def set_availability(self, status: bool) -> None:
        self._is_available = status


class LibrarySystem:

    def __init__(self):
        self._books = {}

    def create_book(self, book: Book) -> None:
        self._books[book.get_isbn()] = book

    def rent(self, isbn: int) -> None:
        self._books[isbn].set_availability(False)

    def give_back(self, isbn: int) -> None:
        self._books[isbn].set_availability(True)

    def list_available_books(self) -> list:
        available_books = [book for book in self._books.values() if book.get_availability() is True]
        return available_books

    def search_by_isbn(self, isbn_num: int) -> Book:
        for isbn, book in self._books.items():
            if isbn == isbn_num:
                return book

    def search_by_title(self, title_input: str) -> list:
        titles_with_title_input = []
        for book in self._books.values():
            if title_input.lower() in book.get_title().lower():
                titles_with_title_input.append(book)
        return titles_with_title_input

    def search_by_author(self, author_input: str) -> list:
        titles_with_author_input = []
        for book in self._books.values():
            if author_input.lower() in book.get_author().lower():
                titles_with_author_input.append(book)
        return titles_with_author_input

    # Metoda opcjonalna. Jest alternatywą dla serach_by_title i serach_by_author
    def serach_by_keyword(self, keyword: str) -> list:
        titles_with_keyword = []
        for book in self._books.values():
            if (keyword.lower() in book.get_title().lower()) or (keyword.lower() in book.get_author().lower()):
                titles_with_keyword.append(book)
        return titles_with_keyword


legimi = LibrarySystem()
legimi.create_book(Book(9788363014063, 'Zyciologia', 'Milosz', 'Brzezinski'))
legimi.create_book(Book(8370540910, 'Czas pogardy', 'Andrzej', 'Sapkowski'))
legimi.create_book(Book(8307012619, 'Swiadectwo poezji', 'Czeslaw', 'Milosz'))

print("List all available:", legimi.list_available_books(), '\n')
print("Search by ISNB:", legimi.search_by_isbn(8370540910), '\n')
print("Search by title:", legimi.search_by_title("zyc"), '\n')
print("Search by author:", legimi.search_by_author("milosz"), '\n')
print("Search by keyword:", legimi.serach_by_keyword("milosz"), '\n')
