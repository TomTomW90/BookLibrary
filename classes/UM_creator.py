from classes.user_admin import Admin
from classes.user_librarian import Librarian
from classes.user_student import Student


class UMCreator:

    @staticmethod
    def create_student(students_id: int, students_first_name: str, students_last_name: str,
                       students_login: str) -> Student:
        new_student = Student()
        new_student.user_id = students_id
        new_student.user_first_name = students_first_name
        new_student.user_last_name = students_last_name
        new_student.user_login = students_login
        return new_student

    @staticmethod
    def create_librarian(librarian_first_name: str, librarian_last_name: str,
                         librarian_login: str) -> Librarian:
        new_librarian = Librarian()
        new_librarian.user_id = Librarian.user_id
        new_librarian.user_first_name = librarian_first_name
        new_librarian.user_last_name = librarian_last_name
        new_librarian.user_login = librarian_login
        return new_librarian

    @staticmethod
    def create_admin(admin_first_name: str, admin_last_name: str,
                     admin_login: str) -> Admin:
        new_admin = Admin()
        new_admin.user_id = Admin.user_id
        new_admin.user_first_name = admin_first_name
        new_admin.user_last_name = admin_last_name
        new_admin.user_login = admin_login
        return new_admin
