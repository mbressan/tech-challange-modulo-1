from fastapi import APIRouter
from core.request_site import RequestSite
from core.transtormation_data import TransformationData

router = APIRouter(
    prefix="/importacao",
    tags=["importacao"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{ano}/{subopcao}",
            description="Requisitar dados de Importação por <b>ano e subtipo</b>",
            tags=["Importação"],
            summary="Obter dados dos anos de Importação"
            )
async def read_importacao(ano: int, subopcao: str):

    request_site = RequestSite()

    request_site.ano = ano
    request_site.opcao = "opt_05"
    request_site.subopcao = subopcao

    transformer = TransformationData()
    response = request_site.get()
    dado = transformer.transform(response)

    return dado