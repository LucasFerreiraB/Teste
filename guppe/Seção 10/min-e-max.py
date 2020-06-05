"""
Min e max

max() -> Retorna o maio valor em um iteravel ou o maior de dois ou mais elemento.

# Exemplos

lista = [1, 2, 3, 4, 66, 675]
print(max(lista)) # 675

tupla = (1, 2, 3, 4, 66, 675)
print(max(tupla)) # 675

conjunto = {1, 2, 3, 4, 66, 675}
print(max(conjunto)) # 675

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 66, 'f': 675}
print(max(dicionario)) # f

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 66, 'f': 675}
print(max(dicionario.values())) # 675

print(max(3, 34)) # 34

# Faça um programa que receba dois valores do usuario e mostre o maior
vall1 = int(input('Informe o primeiro valor: '))
vall2 = int(input('Informe o segundo valor: '))

print(max(vall1, vall2))

print(max(4, 54, 56))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(3.235, 5.322))

print(max('Luck Ferreira'))

min() -> retorna o menor valor em um iteravel ou o menor de dois ou mais elementos

lista = [1, 2, 3, 4, 66, 675]
print(min(lista)) # 675

tupla = (1, 2, 3, 4, 66, 675)
print(min(tupla)) # 675

conjunto = {1, 2, 3, 4, 66, 675}
print(min(conjunto)) # 675

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 66, 'f': 675}
print(min(dicionario)) # f

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 66, 'f': 675}
print(min(dicionario.values())) # 675

print(min(3, 34)) # 34

# Faça um programa que receba dois valores do usuario e mostre o maior
vall1 = int(input('Informe o primeiro valor: '))
vall2 = int(input('Informe o segundo valor: '))

print(min(vall1, vall2))

print(min(4, 54, 56))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(3.235, 5.322))

print(min('Luck Ferreira')) # Espaço vai ser o menor.

# Outros Exemplos

nomes= ['Lucas', 'Ferreira', 'Dora', 'Tim', 'Oliver']

print(max(nomes)) # Leva em consideração a ordem alfabética = Tim

print(min(nomes)) # Ayra

print(max(nomes, key=lambda nome: len(nome))) # Ordena pelo tamanho do nome

print(min(nomes, key=lambda nome: len(nome))) # Ordena pelo tamanho do nome
"""

musicas = [
    {"Titulo": "DragonBall", "tocou": 3},
    {"Titulo": "DragonBall-Z", "tocou": 2},
    {"Titulo": "DragonBall-GT", "tocou": 4},
    {"Titulo": "Inuyasha", "tocou": 32},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio! Imprima somente o titulo da musica + e - tocada

print(max(musicas, key=lambda musica: musica['tocou'])['Titulo']) # Somente o titulo
print(min(musicas, key=lambda musica: musica['tocou'])['Titulo']) # Somente o titulo

# Desafio! Como encontrar a musica mais tocada e a menos tocada sem usar max() min() e lambda()?

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['Titulo'])

min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['Titulo'])