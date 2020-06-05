"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.

# Exemplo
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla, ou dicionario

print(list(zip1))


zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))

zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

# OBS: O zip() utiliza como parametro o menor tamanho em iteravel. Isso significa que se estiver trabalhando com iteraveis de tamanhos
# diferentes, irá parar quando os elementos do menor iteravel acabar
lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# Podemos utilizar diferentes iteráveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dic = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dic.values())
print(list(zt))

# Lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*dados))) # Para desempacotar utilizamos o (*)
"""

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'lucas']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))

print(list(zip(prova1, prova2))) # 1° parte

print(list(map(lambda nota: max(nota), zip(prova1, prova2)))) # 2° parte

print(dict(zip(alunos, [98, 91, 78]))) # 3° parte