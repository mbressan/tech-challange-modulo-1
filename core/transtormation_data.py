"""
Este módulo contém a classe TransformationData, responsável por transformar os dados da resposta em um formato JSON.

Classes:
    - TransformationData: Classe para transformar dados HTML em JSON.
"""

import json
from bs4 import BeautifulSoup
import pandas as pd

class TransformationData:
    def __init__(self):
        pass

    def transform(self, response):
        """
        Transforma a resposta HTML em um JSON.

        Parâmetros:
            - response (str): Resposta HTML da requisição.

        Retorna:
            - str: Dados transformados em formato JSON.
        """
        soup = BeautifulSoup(response, 'html.parser')

        # Encontra a tabela
        tabela = soup.find(name='table', attrs={'class', 'tb_dados'})

        # Extrai os dados da tabela
        data = []
        colunas = []
        for row in tabela.find_all('tr'):
            if len(colunas) == 0:  # Cria a lista do cabeçalho
                cols = row.find_all('th')
                colunas = [ele.text.strip().replace("\n", "") for ele in cols]  # Usa atribuição direta
            else:  # Cria a lista de dados
                cols = row.find_all('td')
                data_row = [ele.text.strip().replace("\n", "") for ele in cols]
                data.append(data_row)

        # Cria um DataFrame pandas com os dados
        df = pd.DataFrame(data, columns=colunas)
        dado = df.to_dict (orient='dict')
        json_str = json.dumps(dado, ensure_ascii=False)

        return json_str

