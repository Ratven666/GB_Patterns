from abc import ABC, abstractmethod
from copy import deepcopy
from datetime import datetime
from random import random


class Task(ABC):
    """Класс абстрактного задания"""
    auto_id = 0

    def __init__(self):
        self.id = None
        # Название задания
        self.name = None
        # Описание задания
        self.description = None
        # Уникальный вариант задания
        self.unique_mission = None
        # Дата выдачи задания
        self.date_of_issue = None
        # Дата отправки задания на проверку
        self.delivery_date = None
        # Дата принятия задания преподавателем
        self.task_due_date = None
        # Комментарии к заданию
        self.comments = []
        # Ответ на задание
        self.answer = None

    @abstractmethod
    def unique_mission_generator(self):
        """ Здесь должна быть реализованна логика генерации уникальных заданий"""
        pass

    def clone(self):
        return deepcopy(self)

    def give_a_task(self, student):
        """Выдает студенту конкретное уникальное задание"""
        task = self.clone()
        task.unique_mission_generator()
        task.date_of_issue = datetime.now()
        Task.auto_id += 1
        task.id = Task.auto_id
        student.tasks.append(task)

    def __str__(self):
        return f"{self.__class__.__name__}:[id={self.id}, name={self.name}, \n" \
               f"date_of_issue={self.date_of_issue}\n" \
               f"delivery_date={self.delivery_date}\n" \
               f"task_due_date={self.task_due_date}\n" \
               f"unique_mission={self.unique_mission}\n" \
               f"answer={self.answer}\n]"

    def __repr__(self):
        return f"{self.__class__.__name__}:[id={self.id}, name={self.name}]"


class Task1(Task):
    def __init__(self):
        super().__init__()
        self.name = "Задание 1"
        self.description = "В задании 1 Вы должны сделать...."
        self.comments = ["Полезным в выполнении работы может оказаться...",
                         "Ссылки на дополнительные материалы...", ]

    def unique_mission_generator(self):
        self.unique_mission = f"Задание 1 {random()}"


class Task2(Task):
    def __init__(self):
        super().__init__()
        self.name = "Задание 2"
        self.description = "В задании 2 Вы должны сделать...."
        self.comments = ["Полезным в выполнении работы может оказаться...",
                         "Ссылки на дополнительные материалы...", ]

    def unique_mission_generator(self):
        self.unique_mission = f"Задание 2 {random()}"


class TaskFactory:
    __types = {
        "Task_1": Task1,
        "Task_2": Task2
    }

    @classmethod
    def create_task_from_type(cls, type_) -> Task:
        return cls.__types[type_]()
