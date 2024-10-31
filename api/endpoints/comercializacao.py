"""
Este módulo define as rotas e handlers para os dados de Comercialização.

Rotas:
    - /comercializacao/{ano}: Obter dados dos anos de Comercialização.
"""

from typing import Annotated
from fastapi import APIRouter, Path
from core.request_site import RequestSite
from core.transtormation_data import TransformationData
from models.base_model import ComercializacaoModel

router = APIRouter(
    prefix="/comercializacao",
    tags=["Comercialização"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{ano}",
            description="Requisitar dados de Comercialização por <b>ano</b>",
            tags=["Comercialização"],
            summary="Obter dados dos anos de Comercialização"
            )
async def get_comercializacao(
        ano: Annotated[int, Path(title='Selecione o ano', ge=1970, le=2023)]
):
    """
    Handler para obter dados de Comercialização por ano.

    Parâmetros:
        - ano (int): Ano para o qual os dados de Comercialização são requisitados.

    Retorna:
        - JSON: Dados de Comercialização transformados.
    """
    opcao = ComercializacaoModel("Comercialização")
    request_site = RequestSite()

    request_site.ano = ano
    request_site.opcao = str(opcao.name)

    transformer = TransformationData()
    response = request_site.get()
    dado = transformer.transform(response)

    return dado
