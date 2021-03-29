import csv
from classes import Book


class FileHendler:

    def __init__(self, path):
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

    # @staticmethod
    # def export_base_csv(source):
    #     with open('./books_test.csv', mode='w') as fd:
    #         csv_writer = csv.writer(fd, delimiter='|')
    #         for element in source.values():
    #             csv_writer.writerow(f'{element.get_isbn()},{element.get_title()},{element.get_author_name()}')
