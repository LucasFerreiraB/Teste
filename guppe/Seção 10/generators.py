"""
Generators Expression

Em aulas anteriores nós estudamos:
- list Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos;
- Tuple Comprehension; ... porque elas se chamam Generators

nomes = ['Carlos', 'Camila', Carla, Cassiano, 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes])

# Poderiamos ter utilizado Generators
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Mostra quantos bytes á de string 'Geek' está ocupando em memória. Quanto maior, mais espaço ocupa.
print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(90348759374598))

print(getsizeof(True))
"""
# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parametro

from sys import getsizeof

# Gerando uma lista de numeros com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando um set de numeros com List Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando um Dict de numeros com List Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de numeros com List Comprehension
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memórias: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dict Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

# Iterando no Generator

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)