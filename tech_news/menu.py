from sys import stderr


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
    e = "0 1 2 3 4".split(" ")
    entrada = input()
    if entrada not in e:
        print("Opção inválida", file=stderr)
        return -1

    return int(entrada)


submenu = [
    lambda: print("Digite quantas notícias serão buscadas:"),
    lambda: print("Digite o título:"),
    lambda: print("Digite a data no formato aaaa-mm-dd:"),
    lambda: print("Digite a tag:"),
    lambda: print("Digite a categoria:"),
]


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    show_main_menu()
    submenu[captura_entrada()]()


if __name__ == "__main__":
    analyzer_menu()
