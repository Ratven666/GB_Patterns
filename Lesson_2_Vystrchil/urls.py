from datetime import date
from views import Index, Lectures, Tasks, Questions, Contact


# front controller
def data_front(request):
    request["date"] = date.today()


def student_id(request):
    request["id"] = "id"


fronts = [data_front, student_id]

routes = {
    '/': Index(),
    "/index.html/": Index(),
    "/lectures.html/": Lectures(),
    "/tasks.html/": Tasks(),
    "/questions.html/": Questions(),
    "/contact.html/": Contact()
}
