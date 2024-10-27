import requests
from http import HTTPStatus

class RequestSite:
    def __init__(self):
        self.url = None
        self.opcao = None
        self.subopcao = None
        self.ano = None


    def get(self):

        self.url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={self.ano}&opcao={self.opcao}"
        if self.subopcao:
            self.url += f"&subopcao={self.subopcao}"

        headers = {"Accept": "application/json"}
        response = requests.get(self.url) #, headers=headers

        if response.status_code == HTTPStatus.OK:
            return response.text
        else:
            return f"Error: {response.status_code}"
