

class Subject:
    def __init__(self):
        self.observers = []

    def notify(self, subject):
        for item in self.observers:
            item.update(subject)
