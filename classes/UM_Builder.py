from abc import ABC, abstractmethod
from classes.user_admin import Admin
from classes.user_librarian import Librarian
from classes.user_student import Student


class UserBuilder(ABC):

    @property
    @abstractmethod
    def confirm_new_user(self):
        pass

    @abstractmethod
    def add_firs_name(self, first_name: str):
        pass

    @abstractmethod
    def add_last_name(self, last_name: str):
        pass

    @abstractmethod
    def add_login(self, login: str):
        pass

    @abstractmethod
    def add_id(self, *args):
        pass


class AdminBuilder(UserBuilder):

    def __init__(self):
        self._new_admin = None
        self.reset()

    def reset(self) -> None:
        self._new_admin = Admin()

    @property
    def confirm_new_user(self) -> Admin:
        new_user = self._new_admin
        self.reset()
        return new_user

    def add_firs_name(self, first_name: str) -> None:
        self._new_admin.user_first_name = first_name

    def add_last_name(self, last_name: str) -> None:
        self._new_admin.user_last_name = last_name

    def add_login(self, login: str) -> None:
        self._new_admin.user_login = login

    def add_id(self) -> None:
        self._new_admin.generate_user_id()


class LibrarianBuilder(UserBuilder):

    def __init__(self):
        self._new_librarian = None
        self.reset()

    def reset(self) -> None:
        self._new_librarian = Librarian()

    @property
    def confirm_new_user(self) -> Librarian:
        new_user = self._new_librarian
        self.reset()
        return new_user

    def add_firs_name(self, first_name: str) -> None:
        self._new_librarian.user_first_name = first_name

    def add_last_name(self, last_name: str) -> None:
        self._new_librarian.user_last_name = last_name

    def add_login(self, login: str) -> None:
        self._new_librarian.user_login = login

    def add_id(self) -> None:
        self._new_librarian.generate_user_id()


class StudentBuilder(UserBuilder):

    def __init__(self):
        self._new_student = None
        self.reset()

    def reset(self) -> None:
        self._new_student = Student()

    @property
    def confirm_new_user(self) -> Student:
        new_user = self._new_student
        self.reset()
        return new_user

    def add_firs_name(self, first_name: str) -> None:
        self._new_student.user_first_name = first_name

    def add_last_name(self, last_name: str) -> None:
        self._new_student.user_last_name = last_name

    def add_login(self, login: str) -> None:
        self._new_student.user_login = login

    def add_id(self, pesel) -> None:
        self._new_student.user_id = pesel


class UserDirector:

    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> UserBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: UserBuilder) -> None:
        self._builder = builder

    def create_new_employee(self, first_name: str, last_name: str, login: str):
        self.builder.add_firs_name(first_name)
        self.builder.add_last_name(last_name)
        self.builder.add_login(login)
        self.builder.add_id()
        return self.builder.confirm_new_user

    def create_new_student(self, first_name: str, last_name: str, login: str, pesel: int):
        self.builder.add_firs_name(first_name)
        self.builder.add_last_name(last_name)
        self.builder.add_login(login)
        self.builder.add_id(pesel)
        return self.builder.confirm_new_user
