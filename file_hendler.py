import csv
from classes import Book


class FileHendler:

    def __init__(self, path: str):
        self.path = path

    def import_base_csv(self):
        output_list_of_books = {}
        with open(self.path) as fd:
            csv_reader = csv.reader(fd, delimiter='|')
            for row in csv_reader:
                if row:
                    book = Book(int(row[0]), row[1], row[2])
                    output_list_of_books[book.get_isbn()] = book
        return output_list_of_books

    def export_base_csv(self, source: dict) -> None:
        books_list = []
        for book in source.values():
            books_list.append([book.get_isbn(), book.get_title(), book.get_author_name(), book.manage_availability])
        with open(self.path, mode='w') as fd:
            csv_writer = csv.writer(fd, delimiter='|')
            for row in books_list:
                csv_writer.writerow(row)
