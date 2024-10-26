from fastapi import APIRouter
from core.request_site import RequestSite

router = APIRouter(
    prefix="/comercializacao",
    tags=["comercializacao"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{ano}")
async def read_comercializacao(ano: int):

    request_site = RequestSite()

    request_site.ano = ano
    request_site.opcao = "opt_04"


    return request_site.get()
