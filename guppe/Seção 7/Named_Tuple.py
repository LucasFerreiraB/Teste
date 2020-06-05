"""
Modulo Collections - Named Tuple

# Recap tupla
tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tupla, diferenciadas, onde, especificamos um nome para a mesma e tambem parametros.
"""
# importando

from collections import namedtuple

# Precisamos definir o nome e parametros

# Forma 1 - declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

# Acessando os dados
# Forma 1

print(ray[0])  # idade
print(ray[1])  # raca
print(ray[2])  # nome
print(f'\n')

# Forma 2

print(ray.idade)  # idade
print(ray.raca)  # raca
print(ray.nome)  # nome
print(f'\n')

print(ray.index('Chow-Chow'))  # Posição do valor
print(ray.count('Chow-Chow'))  # Quantidade do valor


