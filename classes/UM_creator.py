from classes.lib_data import LibraryData
from classes.user_admin import Admin
from classes.user_librarian import Librarian
from classes.user_student import Student


class UMCreator:

    def __init__(self, lib: LibraryData):
        self._lib = lib

    def create_student(self, students_id: int, students_first_name: str, students_last_name: str,
                       students_login: str) -> None:
        new_student = Student()
        new_student.user_id = students_id
        new_student.user_first_name = students_first_name
        new_student.user_last_name = students_last_name
        new_student.user_login = students_login
        self._lib.students[students_id] = new_student

    def create_librarian(self, librarian_id: int, librarian_first_name: str, librarian_last_name: str,
                         librarian_login: str) -> None:
        new_librarian = Librarian()
        new_librarian.user_id = Librarian.user_id
        new_librarian.user_first_name = librarian_first_name
        new_librarian.user_last_name = librarian_last_name
        new_librarian.user_login = librarian_login
        self._lib.librarians[librarian_id] = new_librarian

    def create_admin(self, admin_id: int, admin_first_name: str, admin_last_name: str,
                     admin_login: str) -> None:
        new_admin = Admin()
        new_admin.user_id = Admin.user_id
        new_admin.user_first_name = admin_first_name
        new_admin.user_last_name = admin_last_name
        new_admin.user_login = admin_login
        self._lib.librarians[admin_id] = new_admin
