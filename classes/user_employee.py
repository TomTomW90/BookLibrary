from classes.user import User


class Employee(User):

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, value) -> None:
        self._user_id = self.generate_user_id()

    def generate_user_id(self) -> str:
        if self._user_first_name == "" or self._user_last_name == "":
            raise ValueError('Both first and last name must be given to generate User_id.')
        # here must be implemented condition that will prevent from duplicating _user_id
        # in case there are two users with the same name
        generated_id = f'{self._user_type[:1]}{self._user_first_name[:1]}{self._user_last_name[:1]}'
        self._user_id = generated_id
