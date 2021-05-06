from classes.UI_employee import UIEmployee


class UILibrarian(UIEmployee):

    def remove_user(self, user_id) -> None:
        user_to_remove = self.lib.users[user_id]
        if user_to_remove.user_type == 'Student':
            try:
                del self.lib.users[user_id]
            except KeyError:
                print(f'Given ID {user_id} not found.')
