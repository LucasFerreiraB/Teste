"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia a Teoria dos Conjuntos da Matematica.

- No Python os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matematica;

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos aramzenar elementos mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves, valores a itens duplicados.

os Conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (sets) e Mapas {dicionarios} em Python:
    - Um dicionario tem chave/valor;
    - Um conjunto tem apenas valor;


# Definindo um conjunto;

# Forma 1

s = set([1, 2, 3, 4, 5, 5,  6, 7, 2, 3]) # Repare que temos valores repetidos, set não imprime valores repetidos.

print(s)
print(type(s))

# Forma 2 = Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Verificar se o elemento esta contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Nao tem o 3')

# Alem de nao termos valores duplicados, tambem nao temos ordens

# Listas aceitam valores duplicados
lista = [99, 2, 34, 23, 12, 1, 44, 5, 34]
print(f' Lista: {lista} com {len(lista)} elementos')

# ||
tupla = (99, 2, 34, 23, 12, 1, 44, 5, 34)
print(f' Tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios nao aceitam chaves duplicadas
dic = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5, 34], 'dict')
print(f' Dicionario: {dic} com {len(dic)} elementos')

# Conjuntos nao aceitam valores duplicados
Conj = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f' Conjunto: {Conj} com {len(lista)} elementos')

# Assim como todos outros conjuntos Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# Informamos  manualmente a cidade de onde vieram

# Adicionamos cada cidade em uma lista python, já que em uma lista podemos adicionar novos elementos e ter repetição

cidades = ['Belo Horizonte', 'Sao Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, unicas, temos

# O que voce faria? Faria um llop na lista?

# Podemos utilizar o set para isso:
print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3, 4}
s.add(5)

print(s)
print(type(s))

# Removendo elementos de um conjunto

s = {1, 2, 3, 4}

# Forma 1

s.remove(3)  # Nao é indice, informamos o valor a ser removido
print(s)  # OBS: nenhum valor é retornado quando removido.

# Forma 2

s.discard(2)
print(s)

# Copiando um conjunto para outro

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s
novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 - Utilizando 'union'

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - utilizando o caractere pipe '|'
unicos2 = estudantes_python | estudantes_java

print(unicos2)

# veja que alguns alunos que estudam python tambem estudam java.

# gerar um conjunto de estudantes que estao em ambos os cursos.

# Forma 1 - utilizando 'intersection'

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando 0 '&'

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Métodos Matematicos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um contendo estudantes do curso de java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Gerar um conjunto de estudantes que nao estao no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# Soma*, MaiorValor*, ValorMinimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

s = {1, 45, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

dic = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5, 34], 'dict')
print(f' Dicionario: {dic} com {len(dic)} elementos')