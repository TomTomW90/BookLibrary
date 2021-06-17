import unittest

from classes.book import Book, BookCreator


class BookTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.book_atributes = {
            'isbn': 9788363014063,
            'title': 'Zyciologia',
            'author_name': 'Milosz Brzezinski',
            }

    def test_if_attr_isbn_is_correct(self):
        book = Book(**self.book_atributes)
        self.assertEqual(book._isbn, self.book_atributes['isbn'])

    def test_if_attr_title_is_correct(self):
        book = Book(**self.book_atributes)
        self.assertEqual(book._title, self.book_atributes['title'])

    def test_if_attr_author_name_is_correct(self):
        book = Book(**self.book_atributes)
        self.assertEqual(book._author_name, self.book_atributes['author_name'])

    def test_if_attr_is_available_name_is_correct(self):
        book = Book(**self.book_atributes)
        book._is_available = False
        self.assertFalse(book._is_available)

    def test_if_attr_is_available_is_true_by_default(self):
        book = Book(**self.book_atributes)
        self.assertTrue(book._is_available)

    def test_attr_isbn_when_int_is_given(self):
        book = Book(**self.book_atributes)
        self.assertIsInstance(book._isbn, int)

    def test_attr_isbn_when_not_int_is_given(self):
        self.book_atributes['isbn'] = 'abc'
        with self.assertRaises(ValueError):
            Book(**self.book_atributes)

    def test_attr_isbn_when_not_int_is_given_error_msg(self):
        self.book_atributes['isbn'] = 'abc'
        with self.assertRaisesRegex(ValueError, "^ISBN is wrong type or empty!$"):
            Book(**self.book_atributes)

    def test_attr_isbn_when_none_type_given_error_msg(self):
        self.book_atributes['isbn'] = None
        with self.assertRaisesRegex(ValueError, "^ISBN is wrong type or empty!$"):
            Book(**self.book_atributes)

    def test_attr_title_when_str_is_given(self):
        book = Book(**self.book_atributes)
        self.assertIsInstance(book._title, str)

    def test_attr_title_when_not_str_is_given(self):
        self.book_atributes['title'] = 123
        with self.assertRaises(ValueError):
            Book(**self.book_atributes)

    def test_attr_title_when_not_str_is_given_error_msg(self):
        self.book_atributes['title'] = 123
        with self.assertRaisesRegex(ValueError, "^Title is not a string or empty!$"):
            Book(**self.book_atributes)

    def test_attr_title_when_none_type_given_error_msg(self):
        self.book_atributes['title'] = None
        with self.assertRaisesRegex(ValueError, "^Title is not a string or empty!$"):
            Book(**self.book_atributes)

    def test_attr_title_can_not_be_empty(self):
        self.book_atributes['title'] = ''
        with self.assertRaisesRegex(ValueError, "^Title is not a string or empty!$"):
            Book(**self.book_atributes)

    def test_attr_author_name_when_str_is_given(self):
        book = Book(**self.book_atributes)
        self.assertIsInstance(book._author_name, str)

    def test_attr_author_name_when_not_str_is_given(self):
        self.book_atributes['author_name'] = 123
        with self.assertRaises(ValueError):
            Book(**self.book_atributes)

    def test_attr_author_name_when_not_str_is_given_error_msg(self):
        self.book_atributes['author_name'] = 123
        with self.assertRaisesRegex(ValueError, "^Author is not a string or empty!$"):
            Book(**self.book_atributes)

    def test_attr_author_name_when_none_type_given_error_msg(self):
        self.book_atributes['author_name'] = None
        with self.assertRaisesRegex(ValueError, "^Author is not a string or empty!$"):
            Book(**self.book_atributes)

    def test_attr_author_name_can_not_be_empty(self):
        self.book_atributes['author_name'] = ''
        with self.assertRaisesRegex(ValueError, "^Author is not a string or empty!$"):
            Book(**self.book_atributes)

    def test_attr_is_available_when_bool_is_given(self):
        book = Book(**self.book_atributes)
        self.assertIsInstance(book._is_available, bool)

    def test_attr_is_available_when_not_bool_is_given(self):
        self.book_atributes['is_available'] = 123
        with self.assertRaises(ValueError):
            Book(**self.book_atributes)

    def test_attr_is_available_when_not_bool_is_given_error_msg(self):
        self.book_atributes['is_available'] = 123
        with self.assertRaisesRegex(ValueError, "^Availability status is not 'True' or 'False'!$"):
            Book(**self.book_atributes)

    def test_attr_is_available_when_none_type_given_error_msg(self):
        self.book_atributes['is_available'] = None
        with self.assertRaisesRegex(ValueError, "^Availability status is not 'True' or 'False'!$"):
            Book(**self.book_atributes)

    def test_if_method_manage_isbn_returns_correct_value(self):
        book = Book(**self.book_atributes)
        self.assertEqual(book.manage_isbn, self.book_atributes['isbn'])

    def test_if_method_manage_title_returns_correct_value(self):
        book = Book(**self.book_atributes)
        self.assertEqual(book.manage_title, self.book_atributes['title'])

    def test_if_method_manage_author_name_returns_correct_value(self):
        book = Book(**self.book_atributes)
        self.assertEqual(book.manage_author_name, self.book_atributes['author_name'])

    def test_if_method_manage_availability_returns_correct_value(self):
        book = Book(**self.book_atributes)
        book.manage_availability = True
        self.assertTrue(book.manage_availability)

    def test_if_method_manage_isbn_modifies_value(self):
        book = Book(**self.book_atributes)
        book.manage_isbn = 123456
        self.assertEqual(book.manage_isbn, 123456)

    def test_if_method_manage_title_modifies_value(self):
        book = Book(**self.book_atributes)
        book.manage_title = "Abcadło"
        self.assertEqual(book.manage_title, "Abcadło")

    def test_if_method_manage_author_name_modifies_value(self):
        book = Book(**self.book_atributes)
        book.manage_author_name = "ALa Kotarska"
        self.assertEqual(book.manage_author_name, "ALa Kotarska")

    def test_if_method_manage_availability_modifies_value(self):
        book = Book(**self.book_atributes)
        book.manage_availability = False
        self.assertFalse(book.manage_availability)

    def test_if_method_repr_returns_correct_value(self):
        book = Book(**self.book_atributes)
        repr_value = f"Book(isbn={book.manage_isbn}, title={book.manage_title}, author_name={book.manage_author_name}, is_available={book.manage_availability})"
        self.assertEqual(repr(book), repr_value)

    def test_if_method_str_returns_correct_value(self):
        book = Book(**self.book_atributes)
        str_value = f"{book.manage_title} / {book.manage_author_name} ; ISBN: {book.manage_isbn}"
        self.assertEqual(str(book), str_value)

    def test_if_method_create_clone_creates_obj_with_same_type(self):
        book = Book(**self.book_atributes)
        book_clone = book.create_clone()
        self.assertEqual(type(book), type(book_clone))


class BookCreatorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.book_atributes = {
            'isbn': 9788363014063,
            'title': 'Zyciologia',
            'author_name': 'Milosz Brzezinski',
            }
        self.book_creator = BookCreator()

    def test_if_attr_prototype_is_book_type(self):
        self.assertIsInstance(self.book_creator._prototype, Book)

    def test_if_method_create_new_book_returns_book_type(self):
        new_book = self.book_creator.create_new_book(**self.book_atributes)
        self.assertIsInstance(new_book, Book)

    def test_if_method_create_new_book_sets_correct_attributes(self):
        new_book = self.book_creator.create_new_book(**self.book_atributes)
        self.assertEqual(new_book.manage_isbn, self.book_atributes['isbn'])
        self.assertEqual(new_book.manage_title, self.book_atributes['title'])
        self.assertEqual(new_book.manage_author_name, self.book_atributes['author_name'])
        self.assertTrue(new_book.manage_availability)


if __name__ == '__main__':
    unittest.main()
