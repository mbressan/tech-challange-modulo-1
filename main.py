from fastapi import FastAPI
from api.endpoints import producao, comercializacao, exportacao, processamento, importacao

app = FastAPI()

app.include_router(producao.router)
app.include_router(comercializacao.router)
app.include_router(exportacao.router)
app.include_router(processamento.router)
app.include_router(importacao.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

