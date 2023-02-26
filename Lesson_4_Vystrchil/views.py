from kmd_framework.templator import render
from patterns.creational_patterns.Engine import Engine

site = Engine()


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


class Lectures:
    def __call__(self, request):
        return '200 OK', render('lectures.html', date=request.get('date', None))


class Tasks:
    def __call__(self, request):
        return '200 OK', render('tasks.html', date=request.get('date', None))


class Questions:
    def __call__(self, request):
        return '200 OK', render('questions.html', date=request.get('date', None))


class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html', date=request.get('date', None))


class GroupsPage:
    def __call__(self, request):
        return '200 OK', render('groups.html', objects_list=site.groups)


class CreateGroup:
    def __call__(self, request):
        if request["method"] == "POST":
            data = request["data"]
            group_type = data["type"]
            site.create_group(group_type)

            return '200 OK', render("groups.html", objects_list=site.groups)
        else:
            return '200 OK', render('create_group.html', date=request.get('date', None))


class GroupList:
    def __call__(self, request):
        try:
            id_ = int(request["request_params"]["id"])
            group = site.find_item_by_type_and_id("group", id_)
            return "200 OK", render("group_list.html",
                                    students=group.students,
                                    teacher=group.teacher,
                                    name=group.name, id=group.id)
        except KeyError:
            return "200 OK", "No courses have been added yet"


class UpdateGroup:
    def __call__(self, request):
        if request["method"] == "POST":

            data = request["data"]
            type_ = data["type"]
            name = data["name"]
            id_ = int(data["id"])

            user = site.create_user(type_, name)
            group = site.find_item_by_type_and_id("group", id_)
            if type_ == "teacher":
                group.appoint_teacher(user)
            elif type_ == "student":
                group.add_student(user)

            return "200 OK", render("group_list.html",
                                    students=group.students,
                                    teacher=group.teacher,
                                    name=group.name, id=group.id)
        else:
            try:
                id_ = int(request["request_params"]["id"])
                group = site.find_item_by_type_and_id("group", id_)
                return "200 OK", render("update_group.html",
                                         id=group.id)
            except KeyError:
                return "200 OK", "No courses have been added yet"
