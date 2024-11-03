"""
Este módulo contém os modelos de dados utilizados na API.

Classes:
    - ProducaoModel: Enum para os dados de Produção.
    - ProcessamentoModel: Enum para os dados de Processamento.
    - ProcessamentoSubModel: Enum para os subtipos de Processamento.
    - ComercializacaoModel: Enum para os dados de Comercialização.
    - ImportacaoModel: Enum para os dados de Importação.
    - ImportacaoSubModel: Enum para os subtipos de Importação.
    - ExportacaoModel: Enum para os dados de Exportação.
    - ExportacaoSubModel: Enum para os subtipos de Exportação.
"""

from enum import Enum

class ProducaoModel(str, Enum):
    opt_02 = "Produção"

class ProcessamentoModel(str, Enum):
    opt_03 = "Processamento"

class ProcessamentoSubModel(str, Enum):
    subopt_01 = "Viníferas"
    subopt_02 = "Americanas e Híbridas"
    subopt_03 = "Uvas de Mesa"
    subpot_04 = "Sem Classificação"

class ComercializacaoModel(str, Enum):
    opt_04 = "Comercialização"

class ImportacaoModel(str, Enum):
    opt_05 = "Importação"

class ImportacaoSubModel(str, Enum):
    subopt_01 = "Vinhos de Mesa"
    subopt_02 = "Espumantes"
    subopt_03 = "Uvas Frescas"
    subopt_04 = "Uvas Passas"
    subopt_05 = "Suco de Uva"

class ExportacaoModel(str, Enum):
    opt_06 = "Exportação"

class ExportacaoSubModel(str, Enum):
    subopt_01 = "Vinhos de Mesa"
    subopt_02 = "Espumantes"
    subopt_03 = "Uvas Frescas"
    subopt_04 = "Suco de Uva"
