from abc import ABC, abstractmethod
from re import match


class UserTemplate(ABC):

    def __init__(self):
        self._user_id = ""
        self._full_name = ""
        self._user_login = ""

    @staticmethod
    def validate_id(user_id):
        pass

    @staticmethod
    def validate_name(given_name: str):
        if isinstance(given_name, str) and match(r'[A-Z][a-z]+', given_name):
            return given_name
        else:
            raise ValueError("Given name is incorrect.")

    @abstractmethod
    def add_full_name(self, first_name: str, last_name: str) -> str:
        self._full_name = f'{self.validate_name(first_name)} {self.validate_name(last_name)}'

    @abstractmethod
    def validate_login(self, user_login: str):
        pass
