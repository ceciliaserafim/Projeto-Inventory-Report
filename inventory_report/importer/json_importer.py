import json
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(file_path) as file_name:
            lista = json.load(file_name)
        return list(lista)
