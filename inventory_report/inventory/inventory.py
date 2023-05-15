from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from ..importer.csv_importer import Csv
from ..importer.json_importer import Json
from ..importer.xml_importer import Xml


class Inventory:
    select_file = {
        ".csv": Csv(),
        "json": Json(),
        ".xml": Xml(),
    }
    reports = {
        "simples": SimpleReport,
        "completo": CompleteReport,
    }

    @classmethod
    def import_data(cls, file_path: str, type: str):
        extension = file_path[-4:]

        if extension not in cls.select_file:
            raise ValueError("Arquivo inválido")
        return cls.reports[type].generate(
            cls.select_file[extension].import_data(file_path)
        )
