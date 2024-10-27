from fastapi import APIRouter
from core.request_site import RequestSite
from core.transtormation_data import TransformationData

router = APIRouter(
    prefix="/processamento",
    tags=["processamento"],
    responses={404: {"description": "Not found"}},
)

"""
opcao = "opt_03"

Viniferas               = "subopt_01"
Americanas e hibridas   = "subopt_02"
Uvas de mesa            = "subopt_03"
Sem classificacao       = "subopt_04"

"""


@router.get("/{ano}/{subopcao}")
async def read_processamento(ano: int, subopcao: str):

    request_site = RequestSite()

    request_site.ano = ano
    request_site.opcao = "opt_02"
    request_site.subopcao = subopcao

    transformer = TransformationData()
    response = request_site.get()
    dado = transformer.transform(response)

    return dado