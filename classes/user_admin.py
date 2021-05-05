from classes.user_employee import Employee


class Admin(Employee):

    _user_type = "Admin"

    def __init__(self):
        super().__init__()
        self._user_id = ""
        self._user_first_name = ""
        self._user_last_name = ""
        self._user_login = ""
