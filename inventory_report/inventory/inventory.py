#from importer.importer import Importer
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory():
    @classmethod
    def import_data(cls, file_path):
        if file_path.endswith(".csv"):
            with open(file_path) as file_csv:
                csv.load(file_csv)
            raise ValueError("Extensão inválida")

    