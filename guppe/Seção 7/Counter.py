"""
Modulo - Counter (Contador)
Collections -> High-Performance Container Datetypes

Counter -> Recebe um interavel como parametro e cria um objeto do tipo Colletions Counter que é parecido com um dicionario , contendo
como chave o elemento da lista passada como parametro e como valor a quantidade de ocorrencias desse elemento.
"""

# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iteravel, aqui usamos uma Lista
lista = [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 4, 5, 2, 3]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

# Exemplo 2
print(Counter('Luck Ferreira'))



from collections import Counter

# Exemplo 3
texto = """trhfthfhggggggggghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhfghfthedgfsiughdiughiudrhgudnbiundocnaoijpowjdapoiuerauwjdicieoifj ierofj oierjioerjgiorj igio ejriog jeroigj eiodpovdk porsmoi mrsoisoiefjsiej fofjo iriosrjio gejrigufgsochdiuhg iurtnhiu tngi  """

palavras = texto.split()

print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as cincos palavras com mais ocorrencias
print(res.most_common(5))
