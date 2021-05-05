from classes.user_employee import Employee


class Librarian(Employee):

    _user_type = "Librarian"

    def __init__(self):
        super().__init__()
        self._user_id = ""
        self._user_first_name = ""
        self._user_last_name = ""
        self._user_login = ""
