from typing import Annotated
from fastapi import APIRouter, Path
from core.request_site import RequestSite
from core.transtormation_data import TransformationData
from models.base_model import ProcessamentoModel, ProcessamentoSubModel

router = APIRouter(
    prefix="/processamento",
    tags=["Processamento"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{ano}/{subopcao}",
            description="Requisitar dados de Processamento por <b>ano e subopção de uvas</b>",
            tags=["Processamento"],
            summary="Obter dados dos anos de Processamento"
            )
async def get_processamento(
        ano:  Annotated[int, Path(title="Selecione o ano", ge=1970, le=2023)],
        subopcao: Annotated[
            (ProcessamentoSubModel | None), Path(title="Selecione a subopção")
        ]):

    opcao = ProcessamentoModel("Processamento")

    request_site = RequestSite()

    request_site.ano = ano
    request_site.opcao = str(opcao.name)
    request_site.subopcao = str(subopcao.name)

    transformer = TransformationData()
    response = request_site.get()
    dado = transformer.transform(response)

    return dado