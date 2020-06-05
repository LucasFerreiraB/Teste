"""
Map

Com map, fazemos mapeamento de valores para função.

import math

def area(r):
    #Calcula a area de um circulo com raio 'r'.
    #return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - map

# Map é uma função que recebe dois parametros: O primeiro a função, o segundo um interável. Retorna um Map Object

areas = map(area, raios) # Map pega cada um dos dados de um iterável(raios) e passar como entrada pra função(area)

print(areas)
print(type(areas))

print(list(areas))

# Forma 3 - Map com Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera.

# Para fixar - Map

# Temos dados iteraveis:

# dados: a1, a2, ..., an

# Temos uma função:

# Função: f(x)

# Utilizamos a função map(f, dados) oonde map irá 'mapear' cada elemento dos dados e aplicar a função.

# O Map Object: f(a1), f(a2), f(...), f(an) = + ou - oque o Map retorna
"""

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 28)]

print(cidades)

# f = 9/5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))



