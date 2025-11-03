# parsers/flake8.py
from .base import BaseParser

class Flake8Parser(BaseParser):
    def parse(self):
        errors = []
        with open(self.file_path, encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(":")
                if len(parts) >= 4:
                    errors.append({
                        "file": parts[0],
                        "line": parts[1],
                        "column": parts[2],
                        "message": parts[3].strip()
                    })
        return errors
