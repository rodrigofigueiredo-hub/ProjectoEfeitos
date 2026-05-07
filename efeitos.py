
from random import shuffle  # importa shuffle para baralhar posições aleatórias
from console_utils import clear_screen, pause, show_msg, ask  # importa funções para consola
from typing import Callable, Iterable  # importa tipos para anotações
import argparse  # importa argumentos de linha de comandos
import time  # importa funções de tempo
import math  # importa funções matemáticas


DEFAULT_LINE_LENGTH = 40  # tamanho padrão da linha
DEFAULT_DELAY = 0.3  # atraso padrão entre animações


def show_menu():  # mostra o menu principal
    linhas = [  # lista das linhas do menu
        "",
        "  EFEITO",
        "",
        "      1 - Diagonal Esquerda",
        "      2 - Diagonal Direita, Texto Invertido",
        "      3 - Diagonais Cruzadas",
        "      4 - Em V",
        "      5 - Escada, Palavras Ordem Inversa",
        "      6 - Deslizante",
        "      7 - Destapa Posições Aleatórias",
        "      8 - Destapa Matriz",
        "      T - Todos",
        "      E - Encerrar",
        ""
    ]

    largura = 70  # largura total da caixa

    show_msg("*" * largura)  # imprime linha superior
    for linha in linhas:  # percorre cada linha do menu
        espacos_vazios = largura - len(linha) - 2  # calcula espaços em falta
        show_msg(f"*{linha}{' ' * espacos_vazios}*")  # imprime linha formatada
    show_msg("*" * largura)  # imprime linha inferior


def show_left_to_right_diagonal_effect(txt: str):  # mostra diagonal da esquerda para a direita
    for i, ch in enumerate(txt):  # percorre cada letra e índice
        show_msg(f"{'.' * i}{ch}")  # imprime pontos antes da letra


def show_right_to_left_diagonal_effect(txt: str):  # mostra diagonal da direita para a esquerda
    for i, ch in enumerate(reversed(txt)):  # percorre texto invertido
        show_msg(f"{'.' * i}{ch}")  # imprime pontos antes da letra


def show_x_cross_effect(txt: str):  # mostra efeito em X
    n = len(txt)  # guarda tamanho do texto

    for i in range(n):  # percorre linhas
        linha = []  # cria lista para a linha atual

        for j in range(n):  # percorre colunas
            if i == j or i + j == n - 1:  # verifica diagonais
                linha.append(txt[i] if i == j else txt[n - 1 - i])  # coloca letra
            else:
                linha.append('.')  # coloca ponto

        show_msg(''.join(linha))  # junta e imprime a linha


def show_v_cross_effect(txt: str):  # mostra efeito em V
    n = len(txt)  # tamanho do texto
    side_pace = 0  # espaços laterais
    mid_space = (n * 2) - 2  # espaços do meio

    for v in range(n):  # percorre linhas
        laft_back = txt[v]  # letra da esquerda
        right_back = txt[n - 1 - v]  # letra da direita

        side = '.' * side_pace  # cria pontos laterais
        middle = '.' * mid_space  # cria pontos centrais

        show_msg(f"{side}{laft_back}{middle}{right_back}")  # imprime linha

        side_pace += 1  # aumenta espaços laterais
        mid_space -= 2  # diminui espaços centrais


def show_stair_effect(txt: str):  # mostra efeito escada
    s = txt.split()  # separa palavras

    for i, word in enumerate(reversed(s)):  # percorre palavras invertidas
        show_msg(f"{'.' * i}{word}")  # imprime com deslocamento


def show_sliding_effect(txt: str, line_len=DEFAULT_LINE_LENGTH, delay=DEFAULT_DELAY):  # mostra efeito deslizante
    try:
        i = 0  # posição inicial

        while True:  # repete até o utilizador parar
            line = ['.'] * line_len  # cria linha com pontos

            for j, ch in enumerate(txt):  # percorre letras do texto
                pos = (i + j) % line_len  # calcula posição
                line[pos] = ch  # coloca letra na posição

            show_msg(''.join(line))  # imprime linha
            time.sleep(delay)  # espera
            clear_screen()  # limpa ecrã

            i = (i + 1) % line_len  # avança posição

    except KeyboardInterrupt:  # quando utilizador faz Ctrl+C
        show_msg(''.join(line))  # mostra última linha
        pause()  # pausa


def show_uncover_line_effect(txt: str, delay=DEFAULT_DELAY, speed_up=1.0):  # destapa texto em posições aleatórias
    delay /= speed_up  # ajusta velocidade

    random_positions = list(range(len(txt)))  # cria lista de posições
    shuffle(random_positions)  # mistura posições

    uncovered_line = ['.'] * len(txt)  # cria linha tapada

    for pos in random_positions:  # percorre posições aleatórias
        uncovered_line[pos] = txt[pos]  # revela letra
        show_msg(''.join(uncovered_line))  # imprime linha
        time.sleep(delay)  # espera


def show_uncover_matrix_effect(txt: str, delay=DEFAULT_DELAY, speed_up=1.0):  # destapa texto numa matriz
    delay /= speed_up  # ajusta velocidade

    random_len = len(txt)  # tamanho do texto

    if random_len == 0:  # se estiver vazio
        return  # termina

    size = math.ceil(math.sqrt(random_len))  # calcula tamanho da matriz

    uncovered_matrix = [['.' for _ in range(size)] for _ in range(size)]  # cria matriz com pontos

    random_pos = list(range(len(txt)))  # cria posições
    shuffle(random_pos)  # mistura posições

    for pos in random_pos:  # percorre posições aleatórias
        row = pos // size  # calcula linha
        col = pos % size  # calcula coluna

        uncovered_matrix[row][col] = txt[pos]  # revela letra

        show_msg('\n'.join(''.join(row) for row in uncovered_matrix))  # imprime matriz
        time.sleep(delay)  # espera

    show_msg('\n' + txt)  # imprime texto final


def get_all_effects() -> list[tuple[str, Callable[[Iterable[str]], None]]]:  # devolve lista de efeitos
    return [
        ("Diagonal Esquerda", show_left_to_right_diagonal_effect),
        ("Diagonal Direita", show_right_to_left_diagonal_effect),
        ("Diagonais Cruzadas (X)", show_x_cross_effect),
        ("Efeito em V", show_v_cross_effect),
        ("Escada", show_stair_effect),
        ("Deslizante", show_sliding_effect),
        ("Destapa Aleatório", show_uncover_line_effect),
        ("Destapa Matriz", show_uncover_matrix_effect),
    ]


def show_all_effects(txt: str):  # executa todos os efeitos
    all_effects_list = get_all_effects()  # obtém lista de efeitos

    for effect in all_effects_list:  # percorre efeitos
        name, func = effect  # separa nome e função

        show_msg(f"\n=== {name} ===")  # mostra nome

        func(txt)  # executa efeito

        if func != show_sliding_effect:  # se não for o deslizante
            pause()  # pausa


def main():  # função principal
    parser = argparse.ArgumentParser(
        description='Efeitos especiais para texto na consola'
    )  # cria parser de argumentos

    parser.add_argument(
        '-i', '--delay',
        help='intervalo entre animações (em segundos)',
        type=float,
        default=DEFAULT_DELAY,
        metavar='INTERVALO'
    )  # argumento do atraso

    parser.add_argument(
        '-d', '--line_len',
        help='tamanho da linha do efeito deslizante',
        type=int,
        default=DEFAULT_LINE_LENGTH,
        metavar='DIMENSAO'
    )  # argumento do tamanho da linha

    parser.add_argument(
        'text',
        help='texto a mostrar',
        metavar='TEXTO',
        nargs='+'
    )  # argumento do texto

    args = parser.parse_args()  # lê argumentos

    txt = ' '.join(args.text)  # junta palavras numa string
    delay = args.delay  # guarda atraso
    line_len = args.line_len  # guarda dimensão

    clear_screen()  # limpa ecrã

    while True:  # repete até encerrar
        show_menu()  # mostra menu

        opcao = input("\nEscolha uma opção: ").strip().upper()  # lê opção

        clear_screen()  # limpa ecrã

        if opcao == 'E':  # encerrar
            show_msg("A encerrar o programa...")
            break

        elif opcao == '1':  # diagonal esquerda
            show_msg("=> Diagonal Esquerda")
            show_left_to_right_diagonal_effect(txt)

        elif opcao == '2':  # diagonal direita
            show_msg("=> Diagonal Direita")
            show_right_to_left_diagonal_effect(txt)

        elif opcao == '3':  # diagonais cruzadas
            show_msg("=> Diagonais Cruzadas (X)")
            show_x_cross_effect(txt)

        elif opcao == '4':  # efeito em V
            show_msg("=> Efeito em V")
            show_v_cross_effect(txt)

        elif opcao == '5':  # escada
            show_msg("=> Escada")
            show_stair_effect(txt)

        elif opcao == '6':  # deslizante
            show_msg("=> Efeito Deslizante (Ctrl+C para parar)")
            show_sliding_effect(txt, line_len=line_len, delay=delay)

        elif opcao == '7':  # destapa aleatório
            show_msg("=> Destapa Posições Aleatórias")
            show_uncover_line_effect(txt, delay=delay)

        elif opcao == '8':  # destapa matriz
            show_msg("=> Destapa Matriz")
            show_uncover_matrix_effect(txt, delay=delay)

        elif opcao == 'T':  # executa todos
            show_all_effects(txt)

        else:  # opção inválida
            show_msg("Opção inválida!")

        if opcao != 'T' and opcao != '6':  # evita pausa em modos especiais
            pause()


if __name__ == "__main__":  # verifica se o ficheiro foi executado diretamente
    main()  # chama a função principal

"""
from = importar de...

random = biblioteca para coisas aleatórias

shuffle = baralha a ordem dos elementos de uma lista

console_utils = ficheiro/módulo com funções para a consola

clear_screen = limpa o ecrã

pause = pausa o programa até o utilizador continuar

show_msg = mostra uma mensagem no ecrã

ask = pede informação ao utilizador

typing = biblioteca para indicar tipos de dados

Callable = representa uma função que pode ser chamada

Iterable = representa algo que pode ser percorrido (lista, texto, etc.)

time = biblioteca para trabalhar com tempo

math = biblioteca matemática

DEFAULT_LINE_LENGTH = tamanho padrão da linha

DEFAULT_DELAY = tempo de espera padrão

def = cria uma função

show_menu = nome da função que mostra o menu

linhas = lista com as linhas de texto do menu

largura = largura total da caixa do menu

for = repete um bloco de código

linha = cada linha da lista

len(linha) = quantidade de caracteres da linha

espacos_vazios = quantidade de espaços para completar a largura

show_left_to_right_diagonal_effect = função que mostra diagonal da esquerda para a direita

txt = texto recebido pela função

enumerate(txt) = percorre o texto e devolve posição e letra

i = posição atual

ch = letra atual

'.' * i = repete o ponto i vezes

show_right_to_left_diagonal_effect = mostra diagonal da direita para a esquerda

reversed(txt) = percorre o texto ao contrário

show_x_cross_effect = mostra efeito em X

n = tamanho do texto

range(n) = gera números de 0 até n-1

linha = lista usada para montar uma linha

j = posição da coluna

i == j = diagonal principal

i + j == n - 1 = diagonal secundária

linha.append() = adiciona um elemento à lista

''.join(linha) = junta a lista numa só string

show_v_cross_effect = mostra efeito em V

side_pace = quantidade de pontos do lado

mid_space = quantidade de pontos do meio

v = índice da linha atual

left_back = letra da esquerda

right_back = letra da direita

side = pontos laterais

middle = pontos centrais

show_stair_effect = mostra efeito escada

txt.split() = divide o texto em palavras

word = palavra atual

reversed(s) = percorre as palavras ao contrário

show_sliding_effect = mostra efeito deslizante

line_len = tamanho da linha

delay = tempo de espera

try = tenta executar o código

while True = repete para sempre

line = linha atual

j = posição da letra

pos = posição onde a letra vai aparecer

(i + j) % line_len = faz o texto circular

time.sleep(delay) = espera um tempo

clear_screen() = limpa o ecrã

except KeyboardInterrupt = apanha Ctrl+C do utilizador

show_uncover_line_effect = destapa letras aleatoriamente

speed_up = acelera a animação

delay /= speed_up = diminui o tempo de espera

random_positions = lista de posições

list(range(len(txt))) = cria lista com todas as posições do texto

uncovered_line = linha inicialmente tapada com pontos

pos = posição atual

uncovered_line[pos] = txt[pos] = troca ponto pela letra real

show_uncover_matrix_effect = destapa letras numa matriz

random_len = tamanho do texto

if random_len == 0 = verifica se o texto está vazio

return = termina a função

math.sqrt(random_len) = raiz quadrada do tamanho do texto

math.ceil(...) = arredonda para cima

size = tamanho da matriz

uncovered_matrix = matriz de pontos

random_pos = lista de posições baralhadas

row = linha da matriz

col = coluna da matriz

pos // size = calcula a linha

pos % size = calcula a coluna

uncovered_matrix[row][col] = coloca letra na posição

'\n'.join(...) = junta linhas com quebra de linha

get_all_effects = função que devolve lista de efeitos

list[...] = lista

tuple[...] = conjunto de valores

return = devolve um valor

show_all_effects = executa todos os efeitos

all_effects_list = lista com todos os efeitos

effect = cada efeito

name = nome do efeito

func = função do efeito

func(txt) = executa a função

func != show_sliding_effect = verifica se não é o efeito deslizante

main = função principal

clear_screen() = limpa o ecrã

while True = repete até o utilizador sair

opcao = valor escolhido no menu

input() = lê texto do teclado

strip() = remove espaços no início e no fim

upper() = transforma em maiúsculas

if = condição

elif = outra condição

else = caso nenhuma condição seja verdadeira

break = termina o ciclo

if __name__ == "__main__" = verifica se o ficheiro foi executado diretamente

main() = chama a função principal
"""