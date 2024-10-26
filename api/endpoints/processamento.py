from fastapi import APIRouter
from core.request_site import RequestSite

router = APIRouter(
    prefix="/processamento",
    tags=["processamento"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{ano}/{subopcao}")
async def read_processamento(ano: int, subopcao: str):

    request_site = RequestSite()

    request_site.ano = ano
    request_site.opcao = "opt_02"
    request_site.subopcao = subopcao

    return request_site.get()