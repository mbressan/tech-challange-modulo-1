"""
Este módulo define as rotas e handlers para os dados de Importação.

Rotas:
    - /importacao/{ano}/{subopcao}: Obter dados dos anos de Importação por subtipo.
"""

from typing import Annotated
from fastapi import APIRouter, Path
from core.request_site import RequestSite
from core.transtormation_data import TransformationData
from models.base_model import ImportacaoSubModel, ImportacaoModel

router = APIRouter(
    prefix="/importacao",
    tags=["Importação"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{ano}/{subopcao}",
            description="Requisitar dados de Importação por <b>ano e subtipo</b>",
            tags=["Importação"],
            summary="Obter dados dos anos de Importação"
            )
async def get_importacao(
        ano:  Annotated[int, Path(title="Selecione o ano", ge=1970, le=2023)],
        subopcao: Annotated[
            (ImportacaoSubModel | None), Path(title="Selecione a subopção")]
):
    """
    Handler para obter dados de Importação por ano e subtipo.

    Parâmetros:
        - ano (int): Ano para o qual os dados de Importação são requisitados.
        - subopcao (ImportacaoSubModel): Subtipo de Importação.

    Retorna:
        - JSON: Dados de Importação transformados.
    """
    opcao = ImportacaoModel("Importação")
    request_site = RequestSite()

    request_site.ano = ano
    request_site.opcao = str(opcao.name)
    request_site.subopcao = str(subopcao.name)

    transformer = TransformationData()
    response = request_site.get()
    dado = transformer.transform(response)

    return dado