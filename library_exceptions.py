class EmptyLibraryError(Exception):
    def __init__(self):
        message = 'There is no book in the library. Add a book to the library.'
        super().__init__(message)


class NoAvailBook(Exception):
    def __init__(self):
        message = 'All books are unavailable.'
        super().__init__(message)
