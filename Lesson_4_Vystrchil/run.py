from wsgiref.simple_server import make_server

from kmd_framework.common.variables import PORT
from kmd_framework.main import Framework
from urls import routes, fronts


application = Framework(routes, fronts)

port = 8000

with make_server("", PORT, application) as httpd:
    print(f"Запуск на порту {PORT}...")
    httpd.serve_forever()
