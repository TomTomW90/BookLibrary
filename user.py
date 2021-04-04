from datetime import date as d


class User:

    def __init__(self, pesel: int, user_login: str, full_name: str, date_of_birth: d, main_adress: str, is_blocked: bool, active_loans: list, archive_loans: list):
        self._pesel = self.validate_pesel(pesel)
        self.user_login = user_login  # regex
        self.full_name = full_name  #regex
        self.date_of_birth = date_of_birth
        self.main_adress = main_adress
        self.is_blocked = is_blocked
        self.active_loans = active_loans
        self.archive_loans = archive_loans

    @staticmethod
    def validate_pesel(pesel: int) -> int:
        if not isinstance(pesel, int) or pesel == "":
            raise ValueError("Given PESEL number is not valid.")
        return pesel
