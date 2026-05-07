# Relatório - Projeto Python: Efeitos Especiais

**INSTITUTO DO EMPREGO E FORMAÇÃO PROFISSIONAL (I.E.F.P)**  
**IEFP Alcântara**

**UC:** 00606 - Desenvolver Programas em Linguagens de Estrutura  
**Módulo:** Python  
**Formando:** Rodrigo Figueiredo  
**Nº:** 16  
**Formador:** João Filipe Guimarães Moreira Martins Galamba  
**Data:** 24 / 04 / 2026

---

## 1. Introdução

Este projeto consiste na implementação de um programa em Python capaz de exibir texto através de vários efeitos especiais no terminal. O trabalho foi desenvolvido conforme o enunciado do **Projeto 1 - Efeitos Especiais**, incluindo ainda a implementação de um utilitário da Parte II.

## 2. Estrutura do Projeto

| Ficheiro                  | Descrição |
|---------------------------|---------|
| `efeitos.py`              | Programa principal (menu + 8 efeitos) |
| `console_utils.py`        | Biblioteca de utilitários fornecida pelo formador |
| `tree.py`                 | Utilitário `tree` (Parte II) |
| Fluxogramas (.drawio)     | Documentação visual dos algoritmos principais |
| Docs                      | Relatório |

## 3. Documentação Detalhada do Projeto

### 3.1 Importações e Constantes

- `random.shuffle` → Baralha posições aleatórias (usado nos efeitos 7 e 8)
- `console_utils` → `clear_screen`, `pause`, `show_msg`, etc.
- `argparse` → Lê os parâmetros `-i` (delay) e `-d` (dimensão da linha)
- `time` → Controla a velocidade das animações (`sleep`)
- `math` → Calcula o tamanho da matriz no efeito 8

**Constantes:**
- `DEFAULT_LINE_LENGTH = 40` → Largura da linha no efeito deslizante
- `DEFAULT_DELAY = 0.3` → Tempo padrão entre frames

### 3.2 Funções Principais

| Função                          | Objetivo |
|--------------------------------|----------|
| `show_menu()`                  | Cria e exibe um menu interativo dentro de uma caixa ASCII |
| `show_right_to_left_diagonal_effect()` | Efeito 1 - Diagonal esquerda |
| `show_right_to_left_diagonal_effect()` | Efeito 2 - Diagonal direita (texto invertido) |
| `show_x_cross_effect()`        | Efeito 3 - Diagonais cruzadas em X |
| `show_v_cross_effect()`        | Efeito 4 - Efeito em V |
| `show_stair_effect()`          | Efeito 5 - Efeito escada com palavras invertidas |
| `show_sliding_effect()`        | Efeito 6 - Texto deslizante em ciclo |
| `show_uncover_line_effect()`   | Efeito 7 - Destapa letras aleatoriamente numa linha |
| `show_uncover_matrix_effect()` | Efeito 8 - Destapa letras numa matriz quadrada |
| `show_all_effects()`           | Executa todos os efeitos sequencialmente |
| `main()`                       | Função principal do programa |

### 3.3 Descrição dos Efeitos Implementados

- **Efeito 1:** Cada letra aparece numa nova linha com pontos à esquerda.
- **Efeito 2:** Versão invertida do efeito 1.
- **Efeito 3:** Forma um “X” com as letras do texto.
- **Efeito 4:** As letras formam um “V” (primeira e última letra aproximam-se).
- **Efeito 5:** Palavras são exibidas em escada, pela ordem inversa.
- **Efeito 6:** Texto desliza continuamente numa linha de 40 caracteres (ciclo infinito até Ctrl+C).
- **Efeito 7:** Letras vão sendo reveladas aleatoriamente até o texto ficar completo.
- **Efeito 8:** Versão em matriz quadrada do efeito anterior.

## 5. Fluxogramas Criados

### show_sliding_effect
![Fluxograma - show_sliding_effect](imagens/show_sliding_effect.png)

### show_uncover_line_effect
![Fluxograma - show_uncover_line_effect](imagens/show_uncover_line_effect.png)

### show_uncover_matrix_effect
![Fluxograma - show_uncover_matrix_effect](imagens/show_uncover_matrix_effect.png)

### Função tree
![Fluxograma - Função tree](imagens/funcao_tree.png)

## 6. Funcionalidades Extras

- Menu interativo completo
- Suporte aos parâmetros `-i` e `-d`
- Opção “**T**” → Executar todos os efeitos
- Tratamento robusto de `Ctrl + C` nos efeitos animados
- Uso da função `clear_screen()` otimizada (sem flickering)

## 7. Dificuldades Encontradas e Soluções

| Dificuldade                        | Solução Implementada |
|------------------------------------|----------------------|
| Parar animação com Ctrl+C          | `try / except KeyboardInterrupt` |
| Efeito deslizante contínuo         | Ciclo `while True` + módulo `%` |
| Limpeza de ecrã suave              | Função `clear_screen()` do `console_utils` |
| Cálculo do tamanho da matriz       | `math.ceil(math.sqrt(len(txt)))` |

## 8. Conclusão

Ao concluir este projeto, sinto-me satisfeito com o resultado alcançado. Consegui implementar todos os oito efeitos especiais solicitados, um menu interativo e suporte aos parâmetros de linha de comandos.

Foi um trabalho desafiante, especialmente nos efeitos com animações e no tratamento do Ctrl+C. No entanto, permitiu-me reforçar significativamente os meus conhecimentos em manipulação de strings, listas e módulos como `argparse`, `time` e `random`.

Considero que o projeto cumpriu os objetivos definidos e demonstrou uma boa evolução nas minhas competências em Python. Fico orgulhoso do trabalho final.