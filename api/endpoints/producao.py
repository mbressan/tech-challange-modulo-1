from typing import Annotated
from fastapi import APIRouter, Path
from core.request_site import RequestSite
from core.transtormation_data import TransformationData
from models.base_model import ProducaoModel

router = APIRouter(
    prefix="/producao",
    tags=["Produção"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{ano}",
            description="Requisitar dados de Produção por <b>ano</b>",
            tags=["Produção"],
            summary="Obter dados dos anos de Produção"
            )
async def get_producao(
        ano: Annotated[int, Path(title='Selecione o ano', ge=1970, le=2023)]
):

    opcao = ProducaoModel('Produção')
    request_site = RequestSite()

    request_site.ano = ano
    request_site.opcao = str(opcao.name)

    transformer = TransformationData()
    response = request_site.get()
    dado = transformer.transform(response)

    return dado
