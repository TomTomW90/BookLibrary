from UI_employee import UIEmployee
from classes.UM_creator import UMCreator


class UIAdmin(UIEmployee):

    def add_librarian(self, librarians_first_name: str, librarians_last_name: str, librarians_login: str) -> None:
        new_librarian = UMCreator.create_librarian(librarians_first_name, librarians_last_name, librarians_login)
        self._lib.librarians[new_librarian.user_id] = new_librarian

    def add_admin(self, admins_first_name: str, admins_last_name: str, admins_login: str) -> None:
        new_admin = UMCreator.create_admin(admins_first_name, admins_last_name, admins_login)
        self._lib.admins[new_admin.user_id] = new_admin

    def edit_user(self, user_to_edit_id) -> None:
        pass

    def remove_user(self, user_to_remove_id) -> None:
        if user_to_remove_id in self._lib.students:
            del self._lib.students[user_to_remove_id]
        if user_to_remove_id in self._lib.librarians:
            del self._lib.librarians[user_to_remove_id]
        if user_to_remove_id in self._lib.admins:
            del self._lib.admins[user_to_remove_id]
        else:
            raise KeyError(f'User ID {user_to_remove_id} was not found.')
