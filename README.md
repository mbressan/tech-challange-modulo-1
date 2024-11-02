Projeto é a criação de uma API pública, para consulta de dados do site de Vitivinicultura da Embrapa (http://http://vitibrasil.cnpuv.embrapa.br/):

Os dados que retornam na API são:
    * Produção
    * Processamento
    * Comercialização
    * Importação
    * Exportação

A API servirá para alimentar uma base de dados, que futuramente será usada para um modelo de Machine Learning.

Um pouco sobre como o projeto está estruturado:
    
A API foi desenvolvida em Python, utilizando o framework FastApi. 
A estrutura de pastas utilizada é a recomendada pela documentção do FastApi, onde:
    * api: Onde está o codigo dos Endpoints e o main.py
        *  endpoint: os modulos de cada endpoint
    * core: onde estão as duas princiais classes do projeto:
            request_site: responsavel pela requisição dos dados do site da Embrapa
            transformation_data: responsavel pela transformação dos dados
    * models: Onde estão os modelos e enums de dados
    * tests: Onde estão os testes da API
    * requirements.txt: Arquivo com as dependências do projeto
    * README.md: Arquivo com a descrição do projeto

A API foi publicada no Render.com, nesse endereço é possivel acessar o Swagger da API:
    https://tech-challenge-modulo-1.onrender.com/docs

O projetos pode ser rodado localmente, para isso, basta seguir os passos abaixo:
    * clonar o repositório
    * instalar as dependências 
    * rodar o comando: uvicorn api.main:app --reload



