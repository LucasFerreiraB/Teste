"""
Tipo String

Em python, um dado é considerado do tipo string sempre que:

-Estiver entre aspas simples -> 'uma string', '234', 'True', '42.3'
-Estiver entre aspas duplas -> "uma string", "234", "True", "42.3"
-Estiver entre aspas simples triplas -> '''uma string''', '''234', '''True''', '''42.3'''

nome = 'geek university'
print(nome)
print(type(nome))

nome = "Lucas' s Bar"
print(nome)
print(type(nome))

nome = 'Lucas Ferreira \n Barros'
print(nome)
print(type(nome))

nome = "Lucas \" Ferreira"
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome.upper())

print(nome.lower())

print(nome.split()) # Trasnforma em uma lista de strings

print(nome[0:4])  # Slice de string

print(nome[5:15])  # Slice de string

# [  0,        1]
# ['Geek', 'University']
print(nome.split()[0])

print(nome.split()[1])
"""
# Estiver entre aspas duplas triplas -> """uma string""", """234""", """True""", """42.3"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14 ]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = 'Geek University'

"""
[::-1] -> comece do primeiro elemento, vá até o ultimo elemento e inverta
"""
print(nome[::-1])  # Inversão da String Pythonico

print(nome.replace('e', 'i'))

print(type(nome))

texto = 'socorram-me subino onibus em marrocos'
print(texto)

print(texto[::-1])

nome = 'ana'
print(nome)

print(nome[::-1])
