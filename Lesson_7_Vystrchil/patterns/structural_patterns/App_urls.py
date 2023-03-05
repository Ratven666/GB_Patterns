
class AppUrls:

    def __init__(self, urls, routes):
        self.__urls = urls
        self.__routes = routes

    def __call__(self, view_class):
        for url in self.__urls:
            self.__routes[url] = view_class()
