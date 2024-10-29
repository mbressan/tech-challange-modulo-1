from fastapi import FastAPI
from api.endpoints import producao, comercializacao, exportacao, processamento, importacao

app = FastAPI()

@app.get("/", tags=["Default"], summary="Página Inicial")
async def route_default():
    return "API Embrapa - Tech Challenge"

app.include_router(producao.router)
app.include_router(comercializacao.router)
app.include_router(exportacao.router)
app.include_router(processamento.router)
app.include_router(importacao.router)

