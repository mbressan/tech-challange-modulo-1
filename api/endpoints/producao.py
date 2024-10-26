from fastapi import APIRouter
from core.request_site import RequestSite

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
    return request_site.get()