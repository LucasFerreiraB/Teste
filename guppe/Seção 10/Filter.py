"""
Filter

filter() -> serve para filtrar dados de uma determinada coleção.

# Exemplo
#valores = 1, 2, 3, 4, 5, 6

#media = (sum(valores) / len(valores))

#print(media)

# Biblioteca trabalhar com dados estatísticos
import statistics

#dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean() (mean = media)
media = statistics.mean(dados)

print(f'Média: {media}')
# OBS: Assim como a função map(), a filter() recebe dois parametros, sendo uma função e um iteravel.

res = filter(lambda valor: valor > media, dados)  # função lambda vai receber um valor e retornar somente o valor que for acima da media desses dados.
print(list(res))

print(f'Novamente: {list(res)}') # OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluidos.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Collombia', '', 'Equador', '', '', 'Venezuela']

print(paises)
res = filter(None, paises)

print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Collombia', '', 'Equador', '', '', 'Venezuela']

# res = filter(lambda pais: len(pais) >0, paises)
res = filter(None, paises) # Jeito mais prático.
#res = filter(lambda pais: pais != '', paises)

print(list(res))

# A diferença entre map() e filter() é:

#  map() -. Recebe dois parametros, uma função e um iteravel e retorna um objeto mapeando a função para cada elemento do iteravel.

# filter() -> Recebe dois parametros, uma função e um iteravel e retorna um objeto filtrando apenas os elementos de acordo com a função.

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo bolos", "Eu adoro pizzas"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "dog", "tweets": []},
    {"username": "gal", "tweets": []}
]

print(usuarios)

# Filtrar os usuarios que estao inativos no twitter

# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)
"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua Instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
