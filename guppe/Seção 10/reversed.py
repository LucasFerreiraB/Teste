"""
Reversed

OBS: não confunda com a função reverse()

A função Reverse() só funciona em listas, já a função reversed() funciona em qualquer iteravel.
Sua função é inverter o iterável.

A função reversed() retorna um iteravel chamado: List Reverse Iterator.
"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto - (Set) = 'Set' não define Ordem.
print(set(reversed(lista)))

# Podemos iterar sobre o reversed()
for letra in reversed('Lucas Ferreira'):
    print(letra, end='')
print('\n')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Lucas Ferreira'))))

# Já vimos como fazer isso mais facil com o slice de strings
print('Lucas Ferreira' [::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

print('\n')

# Apesar que também já vimos como fazer isso utilizando o própio range()
for n in range(9, -1, -1):
    print(n)