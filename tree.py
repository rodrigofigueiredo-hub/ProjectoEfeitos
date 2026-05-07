
from pathlib import Path  # importa Path para trabalhar com pastas e ficheiros

def tree(path, prefix=""):  # função que vai mostrar a árvore
    path = Path(path)  # transforma o caminho num objeto Path

    entries = sorted(  # ordena os itens da pasta
        path.iterdir(),  # lista tudo o que está dentro da pasta
        key=lambda p: (p.is_file(), p.name.lower())  # pastas primeiro, depois ficheiros
    )

    for i, entry in enumerate(entries):  # percorre cada item
        connector = "└── " if i == len(entries) - 1 else "├── "  # escolhe o símbolo certo

        print(prefix + connector + entry.name)  # imprime o nome do item

        if entry.is_dir():  # verifica se o item é uma pasta
            extension = "    " if i == len(entries) - 1 else "│   "  # prepara a indentação

            tree(entry, prefix + extension)  # entra na pasta e repete o processo


print(".")  # mostra a pasta atual
tree(".")  # começa a criar a árvore

"""
from = importar de...

pathlib = biblioteca python para caminhos de pastas/ficheiros

Path = representa um caminho

def = cria uma função

tree = nome da função

path = varialvel que recebe a pasta que queres explorar

prefix = texto que vai antes do nome de cada item, vai dar o espaçamento "  "

entries = nome dado à lista de ficheiros e pastas encontradas

sorded(...) = ordena os itens

patch.iterdir() = lista o que esta dentro da pasta

key= = diz ao "sorted" como ordenar

lambda = cria uma função só para usares naquele sitio

p = cada inem da lista

p.is_file() = verifica se é ficheiro

p.name = nome do ficheiro ou pasta

enumerate(entries) = percorre a lista e da o valor e a posição

connector = variavel que guarda o simbolo da arvore

i == len(entries) - 1 = verifica se o item atual é o ultimo

len(entries) = quantidade de itens

prefix + connector + entry.name = junta os simbolos, espaços e o nome

entry.is_dir() = verifica se é uma pasta

extension = guarda a indentação(espaçamentos) do proximo nivel

tree(entry, prefix + extension) = recursão ( entra na pasta, mostra o conteudo e se encontrar outra pasta, entra outra vez)
"""