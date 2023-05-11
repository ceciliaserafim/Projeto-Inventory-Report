from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        rel_simple = super().generate(list)
        produtcs_company = Counter(data["nome_da_empresa"] for data in list)
        rel_simple += "\nProdutos estocados por empresa:\n"

        for company, quantity in produtcs_company.items():
            rel_simple += f"- {company}: {quantity}\n"

        return rel_simple
