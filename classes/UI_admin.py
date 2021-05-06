from classes.UI_employee import UIEmployee
from classes.UM_Builder import UserDirectorForAdmin, AdminBuilder, LibrarianBuilder


class UIAdmin(UIEmployee):

    def add_admin_user(self, first_name: str, last_name: str, login: str):
        director = UserDirectorForAdmin()
        director.builder = AdminBuilder()
        new_admin = director.create_new_employee(first_name, last_name, login)
        self.lib.users[new_admin.user_id] = new_admin

    def add_librarian_user(self, first_name: str, last_name: str, login: str):
        director = UserDirectorForAdmin()
        director.builder = LibrarianBuilder()
        new_librarian = director.create_new_employee(first_name, last_name, login)
        self.lib.users[new_librarian.user_id] = new_librarian

    def remove_user(self, user_id) -> None:
        try:
            del self.lib.users[user_id]
        except KeyError:
            print(f'Given ID {user_id} not found.')
