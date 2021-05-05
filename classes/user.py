from re import match
from abc import ABC, abstractmethod


class User(ABC):

    _user_type = "User"

    def __init__(self):
        self._user_id = ""
        self._user_first_name = ""
        self._user_last_name = ""
        self._user_login_name = ""

    def __str__(self):
        return f'{self._user_type} with ID: {self._user_id}'

    def __repr__(self):
        return f'{self._user_type}(_user_id={self._user_id}, _user_first_name={self._user_first_name}, ' \
               f'_user_last_name={self._user_last_name}, _user_login_name={self._user_login_name}'

    @property
    @abstractmethod
    def user_id(self):
        pass

    @user_id.setter
    @abstractmethod
    def user_id(self, value) -> None:
        pass

    @property
    def user_first_name(self) -> str:
        return self._user_first_name

    @user_first_name.setter
    def user_first_name(self, name: str) -> None:
        self._user_first_name = self.validate_name(name)

    @property
    def user_last_name(self) -> str:
        return self._user_last_name

    @user_last_name.setter
    def user_last_name(self, name: str) -> None:
        self._user_last_name = self.validate_name(name)

    @staticmethod
    def validate_name(given_name: str):
        if isinstance(given_name, str) and match(r'^[A-Z][a-z]+', given_name):
            return given_name
        else:
            raise ValueError("Given name is incorrect.")

    @property
    def user_login(self) -> str:
        return self._user_login_name

    @user_login.setter
    def user_login(self, given_login) -> None:
        self._user_login_name = self.validate_login(given_login)

    @staticmethod
    def validate_login(given_email: str) -> str:
        if isinstance(given_email, str) and match(r'^[\w.-]+@[\w.-]+\.\w+$', given_email):
            return given_email
        else:
            raise ValueError("Given email is incorrect.")

    @property
    def user_type(self) -> str:
        return self._user_type
