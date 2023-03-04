from patterns.creational_patterns.Engine import SingletonMeta


class ConsoleWriter:
    @staticmethod
    def write(text):
        print(text)


class FileWriter:
    def __init__(self):
        self.file_name = "log"

    def write(self, text):
        with open(self.file_name, "a", encoding="utf-8") as f:
            f.write(f"{text}\n")


class Logger(metaclass=SingletonMeta):
    def __init__(self, name, writer=FileWriter()):
        self.name = name
        self.writer = writer

    def log(self, text):
        text = f"log---> {text}"
        self.writer.write(text)
