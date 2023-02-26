# from .Engine import Engine
from patterns.creational_patterns.Engine import Engine

if __name__ == "__main__":
    engine = Engine()

    Engine.create_user("student", "Student_1")
    Engine.create_user("student", "Student_2")
    Engine.create_user("student", "Student_3")

    Engine.create_user("teacher", "Teacher_1")
    Engine.create_user("teacher", "Teacher_2")

    Engine.create_group("mine_survey")
    Engine.create_group("mine_survey")
    Engine.create_group("mine_survey")
    Engine.create_group("survey")

    print(engine)

    group = Engine.find_item_by_type_and_id("group", 1)
    group.add_student(Engine.find_item_by_type_and_id("student", 1))
    group.add_student(Engine.find_item_by_type_and_id("student", 2))
    group.appoint_teacher(Engine.find_item_by_type_and_id("teacher", 1))
    print(group)

    teacher = Engine.find_item_by_type_and_id("teacher", 1)
    teacher.give_the_group_a_task(group, "Task_1")

    student_1 = Engine.find_item_by_type_and_id("student", 1)
    student_2 = Engine.find_item_by_type_and_id("student", 2)
    for task in student_1.tasks:
        print(task)
    print("*" * 50)
    for task in student_2.tasks:
        print(task)

    student_1.send_task(student_1.tasks[0], comment="Не уверен в ответе")

    for task in student_1.tasks:
        print(task.comments)

    teacher.check_task()

    for task in student_1.tasks:
        print(task.comments)

    for task in student_1.tasks:
        print(task)
