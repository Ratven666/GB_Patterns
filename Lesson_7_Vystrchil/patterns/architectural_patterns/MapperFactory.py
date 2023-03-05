from sqlite3 import connect

from kmd_framework.common.variables import DB_NAME
from patterns.architectural_patterns.StudentMapper import StudentMapper
from patterns.creational_patterns.Engine import SingletonMeta
from patterns.creational_patterns.Users import Student


class MapperFactory(metaclass=SingletonMeta):
    mappers = {
        "student": StudentMapper,
    }
    connection = connect(DB_NAME)

    @staticmethod
    def get_mapper(obj):
        if isinstance(obj, Student):
            return StudentMapper(MapperFactory.connection)

    @staticmethod
    def get_current_mapper(name):
        return MapperFactory.mappers[name](MapperFactory.connection)
