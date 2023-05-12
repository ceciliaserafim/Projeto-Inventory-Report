from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(cls, file_path):
        raise NotImplementedError("Você está chamando a classe abstrata")
