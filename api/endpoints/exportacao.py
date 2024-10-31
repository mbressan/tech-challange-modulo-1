"""
Este módulo define as rotas e handlers para os dados de Exportação.

Rotas:
    - /exportacao/{ano}/{subopcao}: Obter dados dos anos de Exportação por subtipo.
"""

from typing import Annotated
from fastapi import APIRouter, Path
from core.request_site import RequestSite
from core.transtormation_data import TransformationData
from models.base_model import ExportacaoSubModel, ExportacaoModel

router = APIRouter(
    prefix="/exportacao",
    tags=["Exportação"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{ano}/{subopcao}",
            description = "Requisitar dados de Exportação por <b>ano e subtipo</b>",
            tags = ["Exportação"],
            summary = "Obter dados dos anos de Exportação"
)
async def get_exportacao(
    ano: Annotated[int, Path(title="Selecione o ano", ge=1970, le=2023)],
    subopcao: Annotated[
        (ExportacaoSubModel | None), Path(title="Selecione a subopção")]
):
    """
    Handler para obter dados de Exportação por ano e subtipo.

    Parâmetros:
        - ano (int): Ano para o qual os dados de Exportação são requisitados.
        - subopcao (ExportacaoSubModel): Subtipo de Exportação.

    Retorna:
        - JSON: Dados de Exportação transformados.
    """
    opcao = ExportacaoModel("Exportação")
    request_site = RequestSite()

    request_site.ano = ano
    request_site.opcao = str(opcao.name)
    request_site.subopcao = str(subopcao.name)

    transformer = TransformationData()
    response = request_site.get()
    dado = transformer.transform(response)

    return dado
