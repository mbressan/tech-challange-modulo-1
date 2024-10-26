from fastapi import APIRouter
from core.request_site import RequestSite

router = APIRouter(
    prefix="/importacao",
    tags=["importacao"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{ano}/{subopcao}")
async def read_importacao(ano: int, subopcao: str):

    request_site = RequestSite()

    request_site.ano = ano
    request_site.opcao = "opt_05"
    request_site.subopcao = subopcao

    return request_site.get()