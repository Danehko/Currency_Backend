# Desafio Estágio uTech

## Regras Gerais
- Você deve criar uma aplicação dividida em Backend e Frontend;
- Você pode utilizar a tecnologia que preferir (Php, Python, Javascript, etc);
- O repositório do desafio deve ser clonado e estar público no github;
- Documente como seu projeto deve ser rodado em ambiente linux (README.md);


## Backend: Criar uma API REST:
- Não é necessário autenticação (api pública);
- Os dados devem ser extraídos de uma api de terceiros (api pública);
- Deve ter 2 ou mais endpoints (rotas);


## Frontend: Criar uma interface WEB:
- Utilize a tecnologia que preferir (react, vue, jquery, vanilla, etc)
- Que consuma a API (backend);
- Que utilize algum framework (bootstrap, materials, html/css puro, etc);
- Que seja responsiva;

Após a conclusão, encaminhar o link do repositório para **estagio@utech.com.br**

Boa sorte!

## Backend

### Requisitos para execução
- Python 3.8.2 (sudo apt-get install python3)
- Criar um ambiente virtual (venv) com as bibliotecas: flask, flask-cors, request
- Instalar a biblioteca simplejson
- Para rodar o Backend: python3 app.py (Foi utilizada a IDE PyCharm)
### Rotas
- http://127.0.0.1:5000/symbols - Rota que lista algumas moedas. Mostrando nome, sigla e símbolo caso possua.
- http://127.0.0.1:5000/convert?from=BRL&to=USD - Rota que converte duas moedas. Para realizar outras conversões basta trocar as siglas do link anterior.
### API de terceiros
- https://free.currconv.com
### Material e Programas de apoio
- Postman
- https://flask-cors.readthedocs.io/en/latest/
