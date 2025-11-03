# main.py
import sys
import os
import pandas as pd
from parsers import Flake8Parser, JacocoParser, SonarParser, ZapParser
from reporter import ReportGenerator

def detect_parser(file_path):
    if file_path.endswith(".log"):
        return Flake8Parser(file_path)
    elif file_path.endswith(".xml") and "jacoco" in file_path:
        return JacocoParser(file_path)
    elif file_path.endswith(".json"):
        return SonarParser(file_path)
    elif file_path.endswith(".xml") and "zap" in file_path:
        return ZapParser(file_path)
    else:
        return None

def main():
    if len(sys.argv) < 2:
        print("❌ Укажите путь к файлу отчёта, например:\n   python main.py examples/flake8.log")
        return

    file_path = sys.argv[1]
    parser = detect_parser(file_path)
    if not parser:
        print("⚠️ Неизвестный формат отчёта.")
        return

    data = parser.parse()
    print(f"✅ Отчёт прочитан! Найдено {len(data)} записей.")

    df = pd.DataFrame(data)
    report = ReportGenerator()
    report.create_html_report(df)
    report.create_pdf_report(df)

if __name__ == "__main__":

    main()