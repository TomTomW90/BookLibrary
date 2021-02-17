import unittest
from classes import LibrarySystem, Book


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

    def test_if_attr_books_is_dict(self):
        library = LibrarySystem()
        self.assertIsInstance(library._books, dict)

    def test_if_method_add_book_to_library_adds_to_attr_books(self):
        library = LibrarySystem()
        book1 = Book(**self.book1_atributes)
        book2 = Book(**self.book2_atributes)
        book3 = Book(**self.book3_atributes)
        library.add_book_to_library(book1)
        library.add_book_to_library(book2)
        library.add_book_to_library(book3)
        self.assertEqual(library._books[self.book1_atributes['isbn']], book1)
        self.assertEqual(library._books[self.book2_atributes['isbn']], book2)
        self.assertEqual(library._books[self.book3_atributes['isbn']], book3)

    def test_if_values_of_attr_books_are_instance_of_book(self):
        library = LibrarySystem()
        book1 = Book(**self.book1_atributes)
        book2 = Book(**self.book2_atributes)
        book3 = Book(**self.book3_atributes)
        library.add_book_to_library(book1)
        library.add_book_to_library(book2)
        library.add_book_to_library(book3)
        self.assertIsInstance(library._books[self.book1_atributes['isbn']], Book)
        self.assertIsInstance(library._books[self.book2_atributes['isbn']], Book)
        self.assertIsInstance(library._books[self.book2_atributes['isbn']], Book)

    def test_if_method_rent_chenges_books_availability(self):
        library = LibrarySystem()
        book1 = Book(**self.book1_atributes)
        book2 = Book(**self.book2_atributes)
        book3 = Book(**self.book3_atributes)
        library.add_book_to_library(book1)
        library.add_book_to_library(book2)
        library.add_book_to_library(book3)
        library.rent(book1._isbn)
        library.rent(book2._isbn)
        library.rent(book3._isbn)
        self.assertEqual(book1.manage_availability, False)
        self.assertEqual(book2.manage_availability, False)
        self.assertEqual(book3.manage_availability, False)


if __name__ == '__main__':
    unittest.main()
