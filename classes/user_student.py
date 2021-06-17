from re import match
from classes.user import User


class Student(User):

    _user_type = "Student"

    def __init__(self):
        super().__init__()
        self._user_id = None
        self._user_first_name = ""
        self._user_last_name = ""
        self._user_login = ""

    def __str__(self):
        return f'{self._user_type} with ID: {self._user_id}'

    def __repr__(self):
        return f'{self._user_type}(_user_id={self._user_id}, _user_first_name={self._user_first_name}, ' \
               f'_user_last_name={self._user_last_name}, _user_login={self._user_login}'

    @property
    def user_id(self) -> int:
        return self._user_id

    @user_id.setter
    def user_id(self, pesel: int) -> None:
        self._user_id = Student.validate_id(pesel)

    @staticmethod
    def validate_id(pesel: int) -> int:
        if not isinstance(pesel, int) or not match(r'\d{11}', str(pesel)):
            raise ValueError("Given PESEL is wrong type or incorrect!")
        return pesel
