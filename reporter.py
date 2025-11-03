import os
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from parsers.flake8 import Flake8Parser

# Основной класс отчётности
class ReportGenerator:
    pdfmetrics.registerFont(TTFont('Arial', 'C:\\Windows\\Fonts\\arial.ttf'))

    def parse_flake8_report(self, file_path):
        parser = Flake8Parser(file_path)
        data = parser.parse()
        print(f"✅ Найдено {len(data)} ошибок Flake8")
        return data

    def __init__(self):
        self.output_folder = "output"
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def load_data(self, file_path):
        if file_path.endswith(".csv"):
            return pd.read_csv(file_path)
        elif file_path.endswith(".json"):
            return pd.read_json(file_path)
        else:
            print("Неподдерживаемый формат файла")
            return None

    def create_html_report(self, data, template_name="template.html"):
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template(template_name)
        html_output = template.render(data=data.to_dict(orient="records"))
        with open(os.path.join(self.output_folder, "report.html"), "w", encoding="utf-8") as f:
            f.write(html_output)
        print("✅ HTML отчёт создан!")

    def create_pdf_report(self, data):
        pdf_path = os.path.join(self.output_folder, "report.pdf")
        pdf = canvas.Canvas(pdf_path, pagesize=letter)
        pdf.setFont("Arial", 12)
        pdf.drawString(100, 760, "Отчёт по данным")
        pdf.setFont("Arial", 10)

        y = 730
        for index, row in data.iterrows():
            text_line = ", ".join([f"{col}: {row[col]}" for col in data.columns])
            pdf.drawString(100, y, text_line)

            y -= 20
            if y < 80:
                pdf.showPage()
                pdf.setFont("Arial", 10)
                y = 750

        pdf.save()
        print("✅ PDF отчёт создан!")

# Тестовый запуск
if __name__ == "__main__":
    report = ReportGenerator()
    data = report.load_data("examples/example.csv")
    if data is not None:
        report.create_html_report(data)
        report.create_pdf_report(data)
