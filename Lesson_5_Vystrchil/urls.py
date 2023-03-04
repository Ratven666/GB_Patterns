from datetime import date
# from views import Index, Lectures, Tasks, Questions, Contact, GroupsPage, CreateGroup, GroupList, UpdateGroup
# from views import Lectures, Tasks, Questions, Contact, GroupsPage, CreateGroup, GroupList, UpdateGroup
#

# front controller
def data_front(request):
    request["date"] = date.today()


def student_id(request):
    request["id"] = "id"


fronts = [data_front, student_id]

# routes = {
#     '/': Index(),
#     "/index/": Index(),
#     "/lectures/": Lectures(),
#     "/tasks/": Tasks(),
#     "/questions/": Questions(),
#     "/contact/": Contact(),
#     "/groups/": GroupsPage(),
#     "/create_group/": CreateGroup(),
#     "/group_list/": GroupList(),
#     "/update_group/": UpdateGroup()
# }

routes = {}
