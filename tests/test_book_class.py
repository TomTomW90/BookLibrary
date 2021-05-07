import unittest

from classes.book import Book


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
        self.assertEqual(book._is_available, False)

    def test_if_attr_is_available_is_true_by_default(self):
        book = Book(**self.book_atributes)
        self.assertEqual(book._is_available, True)

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

    def test_if_method_get_isbn_returns_correct_value(self):
        book = Book(**self.book_atributes)
        self.assertEqual(book.manage_isbn(), self.book_atributes['isbn'])

    def test_if_method_get_title_returns_correct_value(self):
        book = Book(**self.book_atributes)
        self.assertEqual(book.manage_title(), self.book_atributes['title'])

    def test_if_method_get_author_returns_correct_value(self):
        book = Book(**self.book_atributes)
        self.assertEqual(book.manage_author_name(), self.book_atributes['author_name'])

    def test_if_method_manage_availability_returns_correct_value(self):
        book = Book(**self.book_atributes)
        self.assertEqual(book.manage_availability, True)

    def test_if_method_manage_availability_modifies_value(self):
        book = Book(**self.book_atributes)
        book.manage_availability = False
        self.assertEqual(book.manage_availability, False)

    def test_if_method_repr_returns_correct_value(self):
        book = Book(**self.book_atributes)
        repr_value = f"{self.book_atributes['title']} / {self.book_atributes['author_name']} ; ISBN: {self.book_atributes['isbn']}"
        self.assertEqual(str(book), repr_value)


if __name__ == '__main__':
    unittest.main()
