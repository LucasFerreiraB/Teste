"""
Modulo Collections - Default Dict

# Recap Dicionarios
dicio = {'curso': 'Programação em Python'}
print(dicio)

print(dicio['curso'])

Default Dict -> Ao criar um dicionario utilizando-o, nós informamos um valor default, podendo utilizar um lambda para isso.
Este valor será utilizado sempre que nao houver um valor definido. Caso tentamos acessar uma chave que nao existe, essa chave sera
criada e o valor default sera atribuido.

OBS: Lambdas são funções sem nome, que podem ou nao receber parametros de entrada e retornar valores
"""

# Fazendo import
from collections import defaultdict

dicio = defaultdict(lambda: 0)

dicio['curse'] = 'Programação'

print(dicio)

print(dicio['outro'])  # KeyError no Dicionario comum, mas aqui não.

print(dicio)