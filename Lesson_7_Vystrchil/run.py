from wsgiref.simple_server import make_server

from create_db import create_db
from kmd_framework.common.variables import PORT
from kmd_framework.main import Framework
from urls import fronts
from views import routes

application = Framework(routes, fronts)


def run_server(app):
    with make_server("", PORT, app) as httpd:
        print(f"Запуск на порту {PORT}...")
        httpd.serve_forever()


if __name__ == "__main__":
    create_db()
    run_server(application)
