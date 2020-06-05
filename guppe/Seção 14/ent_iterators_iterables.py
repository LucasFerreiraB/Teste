"""
Entendendo Iterators e Iterables

Iterator:
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada:

Iterable:
    - Um objeto que irá retornar um iterator quando a função iter() for chamada:



nome = 'Luck' # É um Iterable mas não é um Iterator.
numeros = [1, 2 ,3 ,4, 5, 6] # É um Iterable mas não é um Iterator.

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
"""

nome = 'Luck'

for letra in nome:
    print(f'{letra}')

    