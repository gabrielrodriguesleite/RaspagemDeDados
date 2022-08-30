# Projeto Tech News - Trybe

Trybe / Desenvolvimento Web / Ciência da computação.

3° Projeto desenvolvido no 4° módulo de Desenvolvimento Web da Trybe (08/22) | Individual.

## Objetivo

Validar o conhecimento sobre raspagem de dados utilizando como fonte o site https://blog.betrybe.com/ e salvar os dados em um banco de dados MongoDB.

## Tecnologias Utilizadas

  - Python3
  - Pytest
  - Black
  - Flake8
  - Docker
  - Docker-compose
  - Linux
  - Git
  - Github

## Resultados Obtidos

<img src="Captura de tela em 2022-08-29 22-50-26.png" alt=""  style="float: right" width="50%" >
<img src="Screenshot 2022-08-29 at 22-52-23 Projeto.png" alt=""  width="49%" >
<img src="Captura de tela em 2022-08-29 23-25-57.png" alt=""  width="100%" >

## Habilidades Desenvolvidas
 
- A organização e a aderência do código à especificação.
- Testes com 90% de coverage(no avaliador da Trybe).
- Técnicas de raspagem de dados extraindo conteúdo HTML.
- Armazenar os dados obtidos em um banco de dados MongoDB.
- Utilizar o terminal interativo do Python3.
- Código limpo e verificado por linter. (Flake8)
 
## Para executar o projeto:

Primeiro execute os containers no docker:

`docker-compose up -d`

Será necessário acoplar ao container tech_news com o comando:

`docker attach tech_news`

Em seguida para executar o projeto use o comando:

`tech-news-analyzer`

Siga as instruções na tela para obter os resultados.

Para derrubar os serviços do docker use o comando:

`docker-compose down --remove-orphans`

## Fontes:

Todos os arquivos que não estiverem listados aqui são de autoria de trybe-teck-ops

Arquivos desenvolvidos por mim:

- README.md

- tech_news/database.py

- tech_news/menu.py

- tech_news/scraper.py

- tech_news/analyzer/ratings.py

- tech_news/analyzer/search_engine.py

- arquivos de imagem png

## TODO:

- Explicação dos módulos do projeto

- Comandos de execução de cada módulo

- Testes