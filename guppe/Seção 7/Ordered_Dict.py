"""
Modulo Collections - OrderedDict

# Ordem nao garantida em um dicionario
dicio = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dicio)

for chave, valor in dicio.items():
    print(f'chave={chave}: valor={valor}')

OrderedDict -> É um dicionario, que nos garante a ordem da inserção dos elementos.

# Fazendo import
from collections import OrderedDict

dicio = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

for chave, valor in dicio.items():
    print(f'chaves = {chave}: valor = {valor}')
"""
from collections import OrderedDict
# Entendendo a diferença entre Dict e OrderedDict

# Dicionario Comum

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True, nao importa pro dicionario comum.

# OrderedDict

edict1 = OrderedDict({'a': 1, 'b': 2})
edict2 = OrderedDict({'b': 2, 'a': 1})

print(edict1 == edict2)  # False, ja que a ordem do elementos importam para o OrderedDict





