"""
Este módulo contém a classe RequestSite, responsável por fazer requisições ao site de Vitivinicultura da Embrapa.

Classes:
    - RequestSite: Classe para fazer requisições HTTP ao site da Embrapa.
"""

import requests
from http import HTTPStatus

class RequestSite:
    def __init__(self):
        self.url = None
        self.opcao = None
        self.subopcao = None
        self.ano = None

    def get(self):
        """
        Faz uma requisição GET ao site da Embrapa com os parâmetros fornecidos.

        Retorna:
            - str: Resposta da requisição em formato de texto ou mensagem de erro.
        """
        try:
            self.url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={self.ano}&opcao={self.opcao}"
            if self.subopcao:
                self.url += f"&subopcao={self.subopcao}"

            headers = {"Accept": "application/json"}
            response = requests.get(self.url, headers=headers)

            if response.status_code == HTTPStatus.OK:
                return response.text
            else:
                return f"Error: {response.status_code}"

        except requests.RequestException as e:
            return f"O Request falhou: {e}"
