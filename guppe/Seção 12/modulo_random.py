"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo random -> possui varias funçãoes para geração de numeros pseudo-aleatório.


# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando todo o módulo. (não recomendado).

import random

#  random() -> Gera um número real pseudo aleatório entre 0 e 1.

# OBS: Ao realizar o import de todo o módulo, todas as funções, atributos, classes, e propiedades que estiverem dentro do módulo ficarão
# disponíveis (ficarão em memória). Caso você saiba quais funções voce precisa utilizar deste módulo, então esta não seria a forma ideal
# de utilização, nós veremos uma forma melho na forma 2.

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função, separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é apenas uma função dentro do
# modulo random.

# Forma 2 - Importando uma função específica do módulo (Forma recomendada)

from random import random

# No import acima, estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())

# uniform() -> gerar um número real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(5, 10))  # 10 não é incluido, valor maximo nunca é mostrado.


# randint() -> gera valores inteiros pseudo-aleatórios entre os valores restabelecidos.
from random import randint

# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')  # "end" = imprime os valores na mesma linha só que com espaço.


# choice() -> Mostra um valor aleatório entre um iterável.
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
print(choice(jogadas))
print(choice('Lucas'))
"""
from random import shuffle
# shuffle() -> Tem a função de embaralhar dados

cartas = ['K', 'Q', 'R', '2', '3', '4', '5']
print(cartas)

shuffle(cartas)

print(cartas.pop())