"""
List Comprehension

- Utilizando list comprehension nós podemos gerar novas listas com dados processdos a partir de outro iteravel.

# Sintax da list comprehension

[dado for dado in iteravel ]

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)


# OBS: para entender melhor acontecendo, devemos dividir a expressão em duas partes:
# - A primeira parte: for numero in numeros
# - A segunda parte: numero * 10

res = [numero / 2 for numero in numeros]
print(res)


def function(valor):
    return valor + valor

res = [function(numero) for numero in numeros]

print(res)

# List Comprehension vs Loop

# Loop
# numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for numero in [1, 2, 3, 4, 5]:
    # numeros_dobrado = numero * 2
    # numeros_dobrados.append(numero_dobrado)
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)


# List Comprehension
# print([numero * 2 for numero in numeros])
print([numero * 2 for numero in [1, 2, 3, 4, 5]])

"""

# Outros exemplos

# 1

nome = 'Geek University'

print([letra.upper() for letra in nome])

# 2

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

print(caixa_alta(nome))

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amigo[0::].upper() for amigo in amigos])
print([caixa_alta(amigo) for amigo in amigos])

# 3

print([args * 3 for args in range(1, 10)])


# 4

print([bool(valor) for valor in [0, [], '', True, 1, 4, 14]])

# 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])


numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)


res = [numero / 2 for numero in numeros]
print(res)


def function(valor):
    return valor + valor

res = [function(numero) for numero in numeros]

print(res)