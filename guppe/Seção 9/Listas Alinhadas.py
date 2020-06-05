"""
Listas Alinhadas (Nested Lists)
- Algumas linguagens de programação possuem uma estrutura de dados chamados de arrays:
    - Unidimensionais (Arrays/Vetores):
    - Multidimensionais (Matrizes):

Em Python nós temos as listas

numeros = [1, 'b', 2.34, True, 4, 5]
"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

print(listas)
print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0][1]) # acesso ao numero 2
print(listas[2][1]) # acesso ao numero 8
print(listas[2][-2]) # acesso ao numero 8

# Iterando com Loops em uma lista alinhada
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension (simplificada)
[[print(valor) for valor in lista] for lista in listas]


