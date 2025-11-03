import os

class BaseParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def exists(self):
        return os.path.exists(self.file_path)

    def parse(self):
        """Переопределяется в наследниках"""
        raise NotImplementedError("Метод parse() нужно реализовать в дочернем классе.")
