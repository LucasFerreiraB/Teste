"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos:

Pacote -> É um diretório contendo uma coleção de módulo:

OBS: Nas versões 2.x do Python, ou seja menor que 3.0, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py

Nas versões do Python 3.x, não é mais obrigatório a utilização deste arquivo, mas normalmente ainda é utilizado para manter compatibilidade


from geek import geek_1, geek_2

from geek.university import geek_3, geek_4

print(geek_1.pi)

print(geek_1.function1(4, 5))

print(geek_2.curso)

print(geek_2.funcao2())

print(geek_3.funcao3())

print(geek_4.funcao4())
"""

from geek.geek_1 import function1
from geek.university.geek_4 import funcao4

print(function1(6, 9))

print(funcao4())
