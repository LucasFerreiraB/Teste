"""
Tuplas (tuple)

tuplas são bastantes parecidas com listas.

existem praticamente duas diferenças basicas:

1 - As tuplas são representadas por parenteses ()

2 - As tuplas são imutaveis: Significa que ao criar uma tupla ela nao muda. Toda operação em uma tupla gera uma nova tupla

# CUIDADO 1: As tuplas representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)  # Isso não é uma tupla!
print(tupla3)

print(type(tupla3))

tupla4 = (4,)  # Isso é uma tupla!
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))
# Conclusão: Podemos concluir que tuplas são definidas mais virgula e não pelo uso do parentese

(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla

# Gerando tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Mochila', 'Magno')

escola, curso = tupla

print(escola)
print(curso)

# Metodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis

# soma*, valor maximo*, valor minimo*, e tamanho

# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Comcatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutaveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla1)
print(tupla2)
print(tupla3)

tupla1 = tupla1 + tupla2  # Tuplas sao imutaveis, mas podemos sobscrever seus valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('a'))

escola = tuple('Luck Ferreira')
print(escola)

print(escola.count('e'))

# Dicas pra utilização de tuplas

# Devemos utilizar tuplas sempre que nao precisarmos modificar dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Junho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Slicing

# Tupla[inicio:fim:passo]

print(meses[0:9])

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual indice um elemento está na tupla

print(meses.index('Junho', 6))

# Caso o elemento não exista será gerado erro

# Por que utilizar tuplas:

# - Tuplas são mais rapidas do que listas.
# - Tuplas deixam seu codigo mais seguro

# Copiar uma tupla para outra

tupla = (1, 2 ,3)
print(tupla)

nova = tupla

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)
"""

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)
