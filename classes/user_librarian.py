from classes.user_template import UserTemplate


class Librarian(UserTemplate):

    _user_type = "Librarian"

    def __init__(self):
        super().__init__()
        self._user_id = ""
        self._user_first_name = ""
        self._user_last_name = ""
        self._user_login = ""

    def __str__(self):
        return f'{self._user_type} with ID: {self._user_id}'

    def __repr__(self):
        return f'{self._user_type}(_user_id={self._user_id}, _user_first_name={self._user_first_name}, ' \
               f'_user_last_name={self._user_last_name}, _user_login={self._user_login}'

    @property
    def user_id(self) -> str:
        return self._user_id

    def generate_user_id(self) -> str:
        if self._user_first_name == "" or self._user_last_name == "":
            raise ValueError('Both first and last name must be given to generate User_id.')
        # here must be implemented condition that will prevent from duplicating _user_id
        # in case there are two users with the same name
        generated_id = f'{self._user_type[:1]}{self._user_first_name[:1]}{self._user_last_name[:1]}'
        self._user_id = generated_id
