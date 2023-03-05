from abc import ABC

from .Users import Student, Teacher
from ..behavioral_patterns.Subject import Subject


class Group(ABC):
    """Класс абстрактной группы"""
    auto_id = 0

    def __init__(self):
        from .Engine import Engine
        Group.auto_id += 1
        self.id = Group.auto_id
        self.name = None
        self.teacher = None
        self.students = []
        self.subject = Subject()
        Engine().groups.append(self)

    @property
    def observers(self):
        return self.subject.observers

    def notify(self):
        self.subject.notify(self.students)

    def add_student(self, student: Student):
        """Добавляет студента в группу"""
        if isinstance(student, Student):
            self.students.append(student)
            student.group = self
            self.notify()
        else:
            raise ValueError("Добавить можно только студентов!")

    def appoint_teacher(self, teacher: Teacher):
        """Назначает группе преподавателя"""
        if self.teacher is None:
            if isinstance(teacher, Teacher):
                self.teacher = teacher
                teacher.groups.append(self)
            else:
                raise ValueError("Добавить можно только преподавателя!")
        else:
            raise ValueError("Преподаватель уже назначен!")

    def __str__(self):
        return f"{self.__class__.__name__}:[id={self.id}, name={self.name}, teacher={self.teacher}\n" \
               f"students={self.students}\n]"

    def __repr__(self):
        return f"{self.__class__.__name__}:[id={self.id}, name={self.name}]"

    def __iter__(self):
        return iter(self.students)


class SurveyGroup(Group):
    __type__ = "survey"
    __counter = 1

    def __init__(self):
        super().__init__()
        self.name = f"ИГ-{SurveyGroup.__counter}"
        SurveyGroup.__counter += 1


class MineSurveyGroup(Group):
    __type__ = "mine_survey"
    __counter = 1

    def __init__(self):
        super().__init__()
        self.name = f"МД-{MineSurveyGroup.__counter}"
        MineSurveyGroup.__counter += 1


class GroupFactory:
    __types = {
        "mine_survey": MineSurveyGroup,
        "survey": SurveyGroup
    }

    @classmethod
    def create_group_from_type(cls, type_):
        group = cls.__types[type_]()
        return group
