from fastapi import APIRouter
from core.request_site import RequestSite
from core.transtormation_data import TransformationData

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
async def read_producao(ano: int):

    request_site = RequestSite()

    request_site.ano = ano
    request_site.opcao = "opt_02"

    transformer = TransformationData()
    response = request_site.get()
    dado = transformer.transform(response)

    return dado
