from kmd_framework.templator import render
from patterns.creational_patterns.Engine import Engine
from patterns.structural_patterns.App_urls import AppUrls
from patterns.structural_patterns.Debug import Debug

site = Engine()
routes = {}


@AppUrls(urls=["/", "/index/"], routes=routes)
class Index:
    @Debug(name="Index", count_number=10)
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


@AppUrls(urls=["/lectures/"], routes=routes)
class Lectures:
    def __call__(self, request):
        return '200 OK', render('lectures.html', date=request.get('date', None))


@AppUrls(urls=["/tasks/"], routes=routes)
class Tasks:
    def __call__(self, request):
        return '200 OK', render('tasks.html', date=request.get('date', None))


@AppUrls(urls=["/questions/"], routes=routes)
class Questions:
    def __call__(self, request):
        return '200 OK', render('questions.html', date=request.get('date', None))


@AppUrls(urls=["/contact/"], routes=routes)
class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html', date=request.get('date', None))


@AppUrls(urls=["/groups/"], routes=routes)
class GroupsPage:
    def __call__(self, request):
        return '200 OK', render('groups.html', objects_list=site.groups)


@AppUrls(urls=["/create_group/"], routes=routes)
class CreateGroup:
    def __call__(self, request):
        if request["method"] == "POST":
            data = request["data"]
            group_type = data["type"]
            site.create_group(group_type)

            return '200 OK', render("groups.html", objects_list=site.groups)
        else:
            return '200 OK', render('create_group.html', date=request.get('date', None))


@AppUrls(urls=["/group_list/"], routes=routes)
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


@AppUrls(urls=["/update_group/"], routes=routes)
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
