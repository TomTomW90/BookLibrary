from typing import Dict
from threading import Lock
from classes.book import Book


class SingletonMeta(type):
    __instance = []
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls.__instance:
                instance = super().__call__(*args, **kwargs)
                cls.__instance = instance
        return cls.__instance


class LibraryData(metaclass=SingletonMeta):

    def __init__(self):
        self._books = {}
        self._users = {}

    @property
    def books(self) -> Dict[int, Book]:
        return self._books

    @property
    def users(self) -> dict:
        return self._users
