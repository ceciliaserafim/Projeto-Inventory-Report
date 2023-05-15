import csv
from .importer import Importer


class Csv(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(file_path) as file_name:
            lista = csv.DictReader(file_name)
            return list(lista)
