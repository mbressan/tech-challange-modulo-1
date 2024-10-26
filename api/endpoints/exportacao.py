from fastapi import APIRouter
from core.request_site import RequestSite

router = APIRouter(
    prefix="/exportacao",
    tags=["exportacao"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{ano}/{subopcao}")
async def read_exportacao(ano: int, subopcao: str):

    request_site = RequestSite()

    request_site.ano = ano
    request_site.opcao = "opt_06"
    request_site.subopcao = subopcao

    return request_site.get()
