import unittest
from classes import LibrarySystem, Book
from library_exceptions import EmptyLibraryError, NoAvailBook


class LibrarySystemTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.book1_atributes = {
            'isbn': 9788363014063,
            'title': 'Zyciologia',
            'author_name': 'Milosz Brzezinski',
            }
        self.book2_atributes = {
            'isbn': 9788375780659,
            'title': 'Krew elfów',
            'author_name': 'Andrzej Sapkowski',
            'is_available': False,
            }
        self.book3_atributes = {
            'isbn': 8307012619,
            'title': 'Świadectwo poezji',
            'author_name': 'Miłosz Czesław',
            'is_available': True,
            }

        self.library = LibrarySystem()

    def test_if_attr_books_is_dict(self):
        self.assertIsInstance(self.library._books, dict)

    def test_if_method_add_book_to_library_adds_to_attr_books(self):

        book1 = Book(**self.book1_atributes)
        book2 = Book(**self.book2_atributes)
        book3 = Book(**self.book3_atributes)
        self.library.add_book_to_library(book1)
        self.library.add_book_to_library(book2)
        self.library.add_book_to_library(book3)

        self.assertEqual(self.library._books[self.book1_atributes['isbn']], book1)
        self.assertEqual(self.library._books[self.book2_atributes['isbn']], book2)
        self.assertEqual(self.library._books[self.book3_atributes['isbn']], book3)

    def test_if_values_of_attr_books_are_instance_of_book(self):

        book1 = Book(**self.book1_atributes)
        book2 = Book(**self.book2_atributes)
        book3 = Book(**self.book3_atributes)
        self.library.add_book_to_library(book1)
        self.library.add_book_to_library(book2)
        self.library.add_book_to_library(book3)

        self.assertIsInstance(self.library._books[self.book1_atributes['isbn']], Book)
        self.assertIsInstance(self.library._books[self.book2_atributes['isbn']], Book)
        self.assertIsInstance(self.library._books[self.book2_atributes['isbn']], Book)

    def test_if_method_rent_chenges_books_availability_to_false(self):

        book1 = Book(**self.book1_atributes)
        book2 = Book(**self.book2_atributes)
        book3 = Book(**self.book3_atributes)
        self.library.add_book_to_library(book1)
        self.library.add_book_to_library(book2)
        self.library.add_book_to_library(book3)
        self.library.rent(book1.get_isbn())
        self.library.rent(book2.get_isbn())
        self.library.rent(book3.get_isbn())

        self.assertEqual(book1.manage_availability, False)
        self.assertEqual(book2.manage_availability, False)
        self.assertEqual(book3.manage_availability, False)

    def test_method_rent_when_isbn_is_not_given(self):
        with self.assertRaisesRegex(ValueError, 'ISBN argument is not given!'):
            self.library.rent("")

    def test_method_rent_when_not_int_is_given(self):
        with self.assertRaisesRegex(ValueError, 'Given ISBN is incorrect type!'):
            self.library.rent('abc')

    def test_method_rent_when_given_isbn_doesnt_exist(self):
        with self.assertRaisesRegex(KeyError, 'Given ISBN does not exist in the library!'):
            self.library.rent(123)

    def test_if_method_give_back_chenges_books_availability_to_true(self):

        book1 = Book(**self.book1_atributes)
        book2 = Book(**self.book2_atributes)
        book3 = Book(**self.book3_atributes)
        self.library.add_book_to_library(book1)
        self.library.add_book_to_library(book2)
        self.library.add_book_to_library(book3)
        self.library.give_back(book1.get_isbn())
        self.library.give_back(book2.get_isbn())
        self.library.give_back(book3.get_isbn())

        self.assertEqual(book1.manage_availability, True)
        self.assertEqual(book2.manage_availability, True)
        self.assertEqual(book3.manage_availability, True)

    def test_method_give_back_when_isbn_is_not_given(self):
        with self.assertRaisesRegex(ValueError, 'ISBN argument is not given!'):
            self.library.give_back("")

    def test_method_give_back_when_not_int_is_given(self):
        with self.assertRaisesRegex(ValueError, 'Given ISBN is incorrect type!'):
            self.library.give_back('abc')

    def test_method_give_back_when_given_isbn_doesnt_exist(self):
        with self.assertRaisesRegex(KeyError, 'Given ISBN does not exist in the library!'):
            self.library.give_back(123)

    def test_if_method_list_available_books_returns_list(self):

        book1 = Book(**self.book1_atributes)
        self.library.add_book_to_library(book1)

        self.assertIsInstance(self.library.list_available_books(), list)

    def test_method_list_available_books_when_books_list_is_empty(self):
        with self.assertRaises(EmptyLibraryError):
            self.library.list_available_books()

    def test_method_list_available_books_when_books_list_is_empty_error_msg(self):
        with self.assertRaisesRegex(EmptyLibraryError, 'There is no book in the library. Add a book to the library.'):
            self.library.list_available_books()

    def test_method_list_available_books_when_returns_empty_list(self):

        book2 = Book(**self.book2_atributes)
        self.library.add_book_to_library(book2)

        with self.assertRaises(NoAvailBook):
            self.library.list_available_books()

    def test_method_list_available_books_when_returns_empty_list_error_msg(self):

        book2 = Book(**self.book2_atributes)
        self.library.add_book_to_library(book2)

        with self.assertRaisesRegex(NoAvailBook, 'All books are unavailable.'):
            self.library.list_available_books()

    def test_if_method_list_available_books_returns_only_available_books(self):

        book1 = Book(**self.book1_atributes)
        book2 = Book(**self.book2_atributes)
        self.library.add_book_to_library(book1)
        self.library.add_book_to_library(book2)
        test_case_list_of_books = [book1]

        self.assertEqual(self.library.list_available_books(), test_case_list_of_books)

    def test_method_search_by_isbn_when_non_int_is_given(self):

        book1 = Book(**self.book1_atributes)
        book1._isbn = 'abc'
        self.library.add_book_to_library(book1)

        with self.assertRaises(ValueError):
            self.library.search_by_isbn('abc')

    def test_method_search_by_isbn_when_empty_str_is_given(self):

        book1 = Book(**self.book1_atributes)
        book1._isbn = ''
        self.library.add_book_to_library(book1)

        with self.assertRaises(ValueError):
            self.library.search_by_isbn('')

    def test_if_method_search_by_isbn_returns_type_book(self):

        book1 = Book(**self.book1_atributes)
        book1._isbn = 123
        self.library.add_book_to_library(book1)

        self.assertIsInstance(self.library.search_by_isbn(123), Book)


if __name__ == '__main__':
    unittest.main()
