from fastapi import APIRouter
from core.request_site import RequestSite
from core.transtormation_data import TransformationData

router = APIRouter(
    prefix="/producao",
    tags=["producao"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{ano}")
async def read_producao(ano: int):

    request_site = RequestSite()

    request_site.ano = ano
    request_site.opcao = "opt_02"

    transformer = TransformationData()
    response = request_site.get()
    dado = transformer.transform(response)

    return dado
