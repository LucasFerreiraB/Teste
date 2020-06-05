"""
Sorted
OBS: não confunda com a função sort() que só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o propio nome diz, sorted() serve para ordenar.

OBS: O sorted, sempre retorna uma lista com os elementos do iteravel ordenados, já o sort modifica a lista.

# Exemplo

numeros = [6, 1, 4, 5]
print(numeros)

print(sorted(numeros)) # Ordenar do menor para o maior

print(numeros)

numeros = [6, 1, 4, 5]

print(tuple(sorted(numeros))) # Convertendo para uma Tupla.

# Adicionando parametros ao sorted

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor
"""
# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo bolos", "Eu adoro pizzas"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "dog", "tweets": []},
    {"username": "gal", "tweets": []}
]
print(usuarios)

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
print(f'\n')
# Ultimo exemplo

musicas = [
    {"Titulo": "DragonBall", "tocou": 3},
    {"Titulo": "DragonBall-Z", "tocou": 2},
    {"Titulo": "DragonBall-GT", "tocou": 4},
    {"Titulo": "Inuyasha", "tocou": 32},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))