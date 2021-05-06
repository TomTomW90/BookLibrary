from classes.UI_employee import UIEmployee
from classes.UM_Builder import UMCreator


class UIAdmin(UIEmployee):

    def add_user(self, user_type: str) -> None:
        user_type = self._lib.users_types[user_type]
        new_user = UMCreator(user_type)

    def edit_user(self, user_to_edit_id) -> None:
        pass

    def remove_user(self, user_to_remove_id) -> None:
        pass
