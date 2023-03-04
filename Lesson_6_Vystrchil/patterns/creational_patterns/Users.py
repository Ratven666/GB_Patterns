from abc import ABC
from datetime import datetime

from .Tasks import TaskFactory, Task


class User(ABC):
    auto_id = 0

    def __new__(cls, *args, **kwargs):
        cls.auto_id += 1
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        self.id = self.auto_id

    def __str__(self):
        return f"{self.__class__.__name__}:[id={self.id}, name={self.name}]"

    def __repr__(self):
        return f"{self.__class__.__name__}:[id={self.id}, name={self.name}]"


class Student(User):
    """Класс студента"""

    def __init__(self, name):
        from .Engine import Engine
        super().__init__(name)
        self.group = None
        self.tasks = []
        Engine().students.append(self)

    def send_task(self, task, comment=None):
        """Отправляет свою работу на проверку"""
        task.answer = input("Введите свой ответ: ")
        if comment is not None:
            task.comments.append(comment)
        task.delivery_date = datetime.now()
        self.group.teacher.tasks_for_verification.append(task)


class Teacher(User):
    """Класс преподавателя"""

    def __init__(self, name):
        from .Engine import Engine
        super().__init__(name)
        # Список задания, что висят на проверку
        self.tasks_for_verification = []
        # Список групп у которых ведет преподаватель
        self.groups = []
        Engine().teachers.append(self)

    def check_task(self):
        """Проверка первой работы из списка"""

        task: Task = self.tasks_for_verification.pop(0)
        for idx, comment in enumerate(task.comments):
            print(idx, comment)
        print(f"ANSWER:\n\t{task.answer}")
        while True:
            result = input("Работа принята? ДА/НЕТ ")
            if result.upper() == "ДА":
                task.comments.append("Работа принята!")
                task.task_due_date = datetime.now()
                break
            elif result.upper() == "НЕТ":
                task.comments.append(input("Укажите причину ошибки... "))
                break
            else:
                print("Вы указали некорректный ответ.")

    def give_the_group_a_task(self, group, type_):
        """Выдача нового задания всей группе"""

        task: Task = TaskFactory.create_task_from_type(type_)
        if group in self.groups:
            for student in group:
                task.give_a_task(student)
        else:
            raise ValueError("Преподаватель не ведет у этой группы")

    def __str__(self):
        return f"{self.__class__.__name__}:[id={self.id}, name={self.name}, groups={self.groups}]"


class UserFactory:
    __types = {
        "student": Student,
        "teacher": Teacher
    }

    @classmethod
    def create_user_from_type(cls, type_, name):
        return cls.__types[type_](name)
