import json
from .base import BaseParser

class SonarParser(BaseParser):
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Проверяем, что формат правильный
        metrics = data.get("metrics", [])
        result = []

        for m in metrics:
            result.append({
                "metric": m.get("metric", "unknown"),
                "value": m.get("value", 0)
            })

        return result
