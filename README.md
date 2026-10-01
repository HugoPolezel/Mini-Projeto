# Mini Projeto: Mangás recentes da Panini

Projeto de Web Scraping da disciplina de Linguagem de Programação II.

## O que faz

Acessa o site da Panini (https://panini.com.br), fecha o aviso de cookies,
entra na seção Planet Mangá, ordena por "Mais recentes" e mostra o nome
e o preço dos 12 primeiros produtos.

## Bibliotecas usadas

- **Selenium**: controla o navegador (fechar cookies, clicar no menu, ordenar).
- **Beautiful Soup (bs4)**: extrai nome e preço do HTML da página.

## Como rodar

1. Instale as bibliotecas:

   python -m pip install -r requirements.txt

2. Execute o script:

   python "Lista de mangás recentes da panini.py"

É necessário ter o Google Chrome instalado.
