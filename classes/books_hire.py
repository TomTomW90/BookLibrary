from datetime import date as d, timedelta as dt
from typing import Union


class Hire:

    def __init__(self):
        self._hire_id = None
        self._hired_book_isbn = None
        self._hiring_users_id = None
        self._start_date: d = None
        self._days_of_hire = None
        self._expected_end_date: d = None
        self._actual_end_date: d = None

    @property
    def hire_id(self) -> int:
        return self._hire_id

    @property
    def hired_book_isbn(self) -> int:
        return self._hired_book_isbn

    @hired_book_isbn.setter
    def hired_book_isbn(self, isbn: int) -> None:
        self._hired_book_isbn = isbn

    @property
    def hiring_user_id(self) -> Union[str, int]:
        return self._hiring_users_id

    @hiring_user_id.setter
    def hiring_user_id(self, user_id: Union[str, int]) -> None:
        self._hiring_users_id = user_id

    @property
    def start_date(self) -> d:
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: d) -> None:
        self._start_date = start_date

    @property
    def days_of_hire(self) -> dt:
        return self._days_of_hire

    @days_of_hire.setter
    def days_of_hire(self, no_of_days: int) -> None:
        self._days_of_hire = dt(days=no_of_days)

    @property
    def expected_end_date(self) -> d:
        return self._expected_end_date

    @expected_end_date.setter
    def expected_end_date(self, no_of_days) -> None:
        self._expected_end_date = self.start_date + no_of_days

    @property
    def actual_end_date(self) -> d:
        return self._actual_end_date

    @actual_end_date.setter
    def actual_end_date(self, actual_end_date: d) -> None:
        self._actual_end_date = actual_end_date

    def create_clone(self):
        from copy import copy
        return copy(self)


class HireCreator:
    _prototype = Hire()

    @staticmethod
    def create_hire(hired_book_isbn: int, hiring_user_id: Union[int, str], start_date: d, no_of_days: int) -> Hire:
        hire_clone = HireCreator()._prototype.create_clone()
        hire_clone.hired_book_isbn = hired_book_isbn
        hire_clone.hiring_user_id = hiring_user_id
        hire_clone.start_date = start_date
        hire_clone.days_of_hire = no_of_days
        return hire_clone
