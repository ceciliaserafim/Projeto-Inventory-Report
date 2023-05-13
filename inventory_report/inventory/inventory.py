from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory():
    @classmethod
    def read_csv(cls, file_path):
        read = csv.DictReader(file_path)
        return list(read)

    @classmethod
    def import_data(cls, file_path, type):
        if not file_path.endswith(".csv"):
            raise ValueError("Extensão inválida")

        with open(file_path) as file_name:
            if file_path.endswith(".csv"):
                lista = Inventory.read_csv(file_name)
                return Inventory.generate_type(type, lista)

    @classmethod
    def generate_type(cls, type, list):
        if type == "simples":
            return SimpleReport.generate(list)
        if type == "completo":
            return CompleteReport.generate(list)


if __name__ == "__main__":
    print(Inventory.read_csv("data/inventory.csv"))
