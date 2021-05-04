from classes.lib_data import LibraryData
from classes.user_student import Student


class UMCreator:

    def __init__(self, lib: LibraryData):
        self._lib = lib
        self._selected_student = None



    def select_student(self, students_id: int) -> None:
        Student.validate_id(students_id)
        modified_student = self._lib.students[students_id]
