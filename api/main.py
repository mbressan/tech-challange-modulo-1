"""
Este módulo inicializa a aplicação FastAPI e define as rotas principais.

Rotas:
    - /: Página inicial da API.
    - /producao: Dados de Produção.
    - /comercializacao: Dados de Comercialização.
    - /exportacao: Dados de Exportação.
    - /processamento: Dados de Processamento.
    - /importacao: Dados de Importação.
"""

from fastapi import FastAPI
from api.endpoints import producao, comercializacao, exportacao, processamento, importacao

app = FastAPI()

@app.get("/", tags=["Default"], summary="Página Inicial")
async def route_default():
    """
    Rota padrão que retorna uma mensagem de boas-vindas.
    """
    return "API Embrapa - Tech Challenge"

app.include_router(producao.router)
app.include_router(comercializacao.router)
app.include_router(exportacao.router)
app.include_router(processamento.router)
app.include_router(importacao.router)
