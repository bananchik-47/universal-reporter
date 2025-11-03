# parsers/zap.py
from .base import BaseParser
import xml.etree.ElementTree as ET

class ZapParser(BaseParser):
    def parse(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        alerts = root.findall(".//alertitem")

        data = []
        for a in alerts:
            data.append({
                "alert": a.findtext("alert"),
                "riskdesc": a.findtext("riskdesc"),
                "desc": a.findtext("desc"),
                "solution": a.findtext("solution"),
                "reference": a.findtext("reference"),
            })
        return data
