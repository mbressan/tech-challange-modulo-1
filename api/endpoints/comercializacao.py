from fastapi import APIRouter
from core.request_site import RequestSite
from core.transtormation_data import TransformationData

router = APIRouter(
    prefix="/comercializacao",
    tags=["Comercialização"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{ano}",
            description="Requisitar dados de Comercialização por <b>ano e subtipo</b>",
            tags=["Comercialização"],
            summary="Obter dados dos anos de Comercialização"
            )
async def read_comercializacao(ano: int):

    request_site = RequestSite()

    request_site.ano = ano
    request_site.opcao = "opt_04"

    transformer = TransformationData()
    response = request_site.get()
    dado = transformer.transform(response)

    return dado
