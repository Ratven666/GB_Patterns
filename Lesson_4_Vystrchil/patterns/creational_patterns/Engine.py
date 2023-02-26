from threading import Lock

from .Groups import GroupFactory
from .Users import UserFactory


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Engine(metaclass=SingletonMeta):
    def __init__(self):
        self.students = []
        self.teachers = []
        self.groups = []

    @staticmethod
    def create_user(type_, name):
        return UserFactory.create_user_from_type(type_, name)

    @staticmethod
    def create_group(type_):
        return GroupFactory.create_group_from_type(type_)

    @classmethod
    def find_item_by_type_and_id(cls, type_, id_):
        types = {"student": cls().students,
                 "teacher": cls().teachers,
                 "group": cls().groups
                 }
        if type_ in types:
            for item in types[type_]:
                if item.id == id_:
                    return item
            raise Exception(f"Нет объекта с таким id = {id_}")
        raise ValueError(f"Нет категории {type_}")

    def __str__(self):
        return f"Engine:[\n" \
               f"\tstudents: {self.students}\n" \
               f"\tteachers: {self.teachers}\n" \
               f"\tgroups: {self.groups}\n" \
               f"]"
