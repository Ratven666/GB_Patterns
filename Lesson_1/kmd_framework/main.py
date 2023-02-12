
class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class Framework:

    """Класс Framework - основа фреймворка"""

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    @staticmethod
    def __path_generator(environ):
        path = environ["PATH_INFO"]
        if not path.endswith("/"):
            path = f"{path}/"
        return path

    def __call__(self, environ, start_response):
        path = self.__path_generator(environ)

        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()
        request = {}

        for front in self.fronts:
            front(request)

        code, body = view(request)
        start_response(code, [("Content-Type", "text/html")])
        return [body.encode("utf-8")]
