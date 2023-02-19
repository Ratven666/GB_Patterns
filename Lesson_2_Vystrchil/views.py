from kmd_framework.templator import render


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
