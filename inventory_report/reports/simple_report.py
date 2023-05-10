from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list):
        # old_manufacturing_date =
        lista = []
        lista_validade = []
        data_atual = datetime.today().date()
        empresas = []

        for data in list:
            lista.append(
                datetime.strptime(
                    data["data_de_fabricacao"], "%Y-%m-%d"
                ).date()
            )

        for data in list:
            date_time = datetime.strptime(
                data["data_de_validade"], "%Y-%m-%d"
            ).date()
            if date_time > data_atual:
                lista_validade.append(date_time)

        for data in list:
            empresas.append(data["nome_da_empresa"])

        frequencia_empresa = Counter(empresas).most_common()
        mais_frequente = frequencia_empresa[0]

        return (f"Data de fabricação mais antiga: {min(lista)}\n"
                f"Data de validade mais próxima: {min(lista_validade)}\n"
                f"Empresa com mais produtos: {mais_frequente[0]}")
    