from classes.UI_employee import UIEmployee
from classes.UM_editor import UMEditor


class UILibrarian(UIEmployee):

    def edit_user(self, student_to_edit_id: int) -> None:
        return UMEditor(student_to_edit_id)

    def remove_user(self, student_to_remove_id: int) -> None:
        try:
            del self._lib.students[student_to_remove_id]
        except KeyError as ke:
            print(f'Student ID not found:{ke.args}')
