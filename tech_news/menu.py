import sys
from tech_news.analyzer.ratings import top_5_categories, top_5_news

from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_category,
    search_by_tag,
    search_by_date,
)
from tech_news.scraper import get_tech_news


def show_main_menu():
    print(
        """\
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.\
"""
    )


def captura_entrada():
    entrada = input()
    return -1 if entrada not in "0 1 2 3 4 5 6 7".split(" ") else int(entrada)


# Requisito 13
def gt_news():
    print("Digite quantas notícias serão buscadas:")
    print(get_tech_news(int(input())))


def sb_title():
    print("Digite o título:")
    search_by_title(input())


def sb_date():
    print("Digite a data no formato aaaa-mm-dd:")
    search_by_date(input())


def sb_tag():
    print("Digite a tag:")
    search_by_tag(input())


def sb_category():
    print("Digite a categoria:")
    search_by_category(input())


submenu = [
    gt_news,
    sb_title,
    sb_date,
    sb_tag,
    sb_category,
    lambda: print(top_5_news()),
    lambda: print(top_5_categories()),
    lambda: print("Encerrando script"),
    lambda: print("Opção inválida", file=sys.stderr),
]


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    show_main_menu()
    submenu[captura_entrada()]()


if __name__ == "__main__":
    analyzer_menu()
