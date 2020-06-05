"""
PEPE - Python Enhancement Proposal
São propostas de melhorias para a linguagem Python
The Zen of Python
import this

A ideia da pep8 é que possamos escrever codigos python de forma pythonica.

[1] - Utilize Camel Case para nomes de classes;
class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - utilize nomes em minusculo, separados por underline para funções ou variaveis;
def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] Utilize 4 espaços para identação  (não use o TAB);

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Metodos dentro de uma classe devem ser separados com uma unica linha em branco;

[5] - Imports
- Imports devem ser sempre feitos em linhas separadas;

# import Errado
import sys, os

# import certo
import sys
import os

# Não há problemas em utilizar;

from types import Stringtype, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer;

from types import (
    StringType,
    ListType,
    SetType,
    Outroype
)

# Import devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes de constantes ou variaveis globais.

[6] - espaços expressões e instrunções

# não faça:

Funcao(_algo[_1_], {_outro: 2_}_)

# Faça:

função(algo[1], {outro: 2})

# Não faça:

algo_(1)

# Faça:

algo(1)

# Não faça:

dict ['chave'] = lista [indice]

# Faça:

dict['chave'] = lista[indice]

# Não faça:

x              = 1
y              = 3
variavel_longa = 5

# Faça:

x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrunção com uma nova linha em branco
'''
- Comentarios de uma linha só
'''
"""
import this




