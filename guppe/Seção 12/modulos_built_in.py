"""
Trabalhando com mmódulos built-in (módulos integrados, que já vem instalados no Python)

/Python/Módulos built-in/
OBS: Já vem instalado mas para se usar, faz o import dos Módulos built-in para usa-los, para não sobrecarregar a memória do python.

# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())


# Podemos importar todas as funções de um módulo utilizando o *

from random import *
# import random

print(random())


# Importando todo o módulo

import random

print(random.random())


# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())

https://docs.python.org/3/py-modindex.html
"""
# Costumamos a utilizar tuple para colocar multiplos imports de um mesmo módulo

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = ['Luck', 'Ferreira', 'Python']
shuffle(lista)
print(lista)

print(choice('Lucas'))