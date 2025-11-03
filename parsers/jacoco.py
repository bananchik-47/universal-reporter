# parsers/jacoco.py
from .base import BaseParser
import xml.etree.ElementTree as ET

class JacocoParser(BaseParser):
    def parse(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        counters = root.findall(".//counter")

        data = []
        for c in counters:
            data.append({
                "type": c.attrib.get("type"),
                "missed": int(c.attrib.get("missed")),
                "covered": int(c.attrib.get("covered")),
            })
        return data
