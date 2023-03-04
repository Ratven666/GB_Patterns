from .GetRequests import GetRequests
from .PostRequests import PostRequests


class PageNotFound404:
    def __call__(self, request):
        return "404 WHAT", "404 PAGE Not Found"


class Framework:
    """Класс Framework - основа фреймворка"""

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        view = self.__view_initiator(environ)

        request = {}

        self.__request_methods(environ, request)
        self.__front_loader(request)

        code, body = view(request)
        start_response(code, [("Content-Type", "text/html")])
        return [body.encode("utf-8")]

    @staticmethod
    def __path_generator(environ):
        path = environ["PATH_INFO"]
        if not path.endswith("/"):
            path = f"{path}/"
        return path

    def __view_initiator(self, environ):
        path = self.__path_generator(environ)
        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()
        return view

    def __front_loader(self, request):
        for front in self.fronts:
            front(request)

    @staticmethod
    def __request_methods(environ, request):
        method = environ["REQUEST_METHOD"]
        request["method"] = method

        if method == "GET":
            request["request_params"] = GetRequests().get_request_params(environ)
            print(f"Нам пришли GET-параметры: {request['request_params']}")
        if method == "POST":
            request["data"] = PostRequests().get_request_params(environ)
            print(f"Нам пришёл POST-запрос: {request['data']}")
