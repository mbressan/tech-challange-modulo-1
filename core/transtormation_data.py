import json

from bs4 import BeautifulSoup
import pandas as pd


class TransformationData:
    def __init__(self):
         ...

    def transform(self, response):
        soup = BeautifulSoup(response, 'html.parser')

        # Encontra a tabela
        tabela = soup.find(name='table',attrs= {'class', 'tb_dados'})

        # Extrai os dados da tabela
        data = []
        colunas = []
        for row in tabela.find_all('tr'):
            if len(colunas) == 0: # Cria a lista do cabeçalho
                cols = row.find_all('th')
                cols = [ele.text.strip() for ele in cols]
                colunas.append([ele for ele in cols if ele])
            else: # Cria a lista de dados
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])

        # Cria um DataFrame pandas com os dados
        df = pd.DataFrame(data, columns=colunas)
        dados = df.to_dict(orient='dict') # df.to_json(orient='records', force_ascii=False)
        json_data = dados.to_json(orient='records', force_ascii=False)
        return json_data


