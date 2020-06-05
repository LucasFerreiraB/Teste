"""
Listas - (list)
Listas são mutaveis

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINAMICO e também de podermos
colocar QUALQUER tipo de dado.

Linguagens C/java: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nestas linguagens se voce criar um array do tipo int e com tamanho 5, este array será SEMPRE do tipo inteiro e poderá ter
SEMPRE no maximo 5 valores.

Já em Python:

- Dinamico: Não possue tamanho fixo: Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dados: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

type([])

lista1 = [1, 99, 4, 27, 25, 22, 3, 1, 44, 42, 27]

lista2 = ['L', 'U', 'C', 'K']

lista3 = []

lista4 = list(range(11))

lista5 = list('LUCK FERREIRA')


# Podemos facilmente checar se determinado valor está contido na lista
num = 'A'
if num in lista2:
    print(f'Encontrei a letra {num}')
else:
    print(f'Não encontrei a letra {num}')

# Podemos facilmente ordernar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('L'))

# Adicionar elementos em listas, para adicionar elementos em listas, utilizamos a função append
# OBS: Com append, só conseguimos adicionar um elemento por vez.
print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1]) # Coloca a lista como elemento único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional a lista. OBS: Não aceita valor único.
print(lista1)

# Podemos inserir um novo elemento na lista informado a posição do indice
# Isso não substitui o valor inicial, o mesmo sera deslocado para a direita da lista.
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntar duas listas:

# Uma opção: lista6 = lista1 + lista2
# Segunda opção: lista1 = lista1 + lista2
# Terceira opção: lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Contar elementos em uma lista, Exemplo:
print(len(lista1))

# Podemos remover facilmente o ultimo elemento de uma lista
# OBS: não só remove, mas tambem o retorna.
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
# OBS: Os elementos à direita deste indice serão deslocados para a esquerda.
lista5.pop(2)
print(lista5)

# Remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python'
print(curso)
curso = curso.split()  # Por padrão, o split separa os elementos da lista pelo espaço entre elas.
print(curso)

# Exemplo 2
curso = 'Programação,em,Python,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

# Colocando espaço em cada elemento e transformando em uma string
curso = ' '.join(lista6)
print(curso)

# Coloca o '$' entre cada elemento e transformando em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'Luck', 'l', [1, 2, 3], 25352352535]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - Utilizando for
soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Add um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de formas indexadas

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos de forma indexada inversa

print(cores[-1])  # Branco
print(cores[-2])  # Azul
print(cores[-3])  # Amarelo
print(cores[-4])  # Verde

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar (CHAVES e VALORES) indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outros metodos nao tao importantes mas tambem uteis:

# encontrar o indice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice da lista está o valor 6?
print(numeros.index(6))

# Em qual indice da lista está o valor 9?
print(numeros.index(9))

# OBS: Caso nao tenha esse elemento na lista, sera apresentado erro.

# OBS: Retorna o indice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))  # busca a partir do indice 1
print(numeros.index(5, 2))  # busca a partir do indice 1
print(numeros.index(5, 3))  # busca a partir do indice 1
# print(numeros.index(5, 4))  # busca a partir do indice 1  # Erro por posição

# Busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) # Busca o indice de valor 8, entre os indices 6 a 8

# Revisao slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# trabalhando com slice de lista com o parametro 'inicio'

lista = [1, 2, 3, 4]

print(lista[0:])  # Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com parametro 'fim'

print(lista[:2])  # começa em 0, pega até o indice 2 - 1

print(lista[:4])  # começa em 0, pega até o indice 4 - 1

print(lista[1:3]) # começa em 0, pega até o indice 3 - 1

# Trabalhando com slice de lista com o parametro 'passo'

print(lista[1::2])  # Começa em 1, vai até o final, 2 em 2

print(lista[::2])  # Começa em 0 , vai até o final, 2 em 2

print(lista[1::-1])  # Começa em 1, e vai até o final, -1 em -1

# Invertendo valores em uma lista

nomes = ['Luck', 'Ferreira', 'Barros']

nomes[0], nomes[1], nomes[2] = nomes[1], nomes[2], nomes[0]

print(nomes)

nomes = ['Luck', 'Ferreira', 'Barros']

nomes.reverse()
print(nomes)

# Soma*, valor maximo*, valor minimo*, tamanho

# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista))  # maximo valor
print(min(lista))  # minimo valor
print(len(lista))  # tamanho da lista

# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(type(tupla))

# Desempacotamento de lista

lista = [0, 1, 2, 3]
num, num1, num2, num3 = lista
print(num)
print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - lista.copy = Deep Copy (copia profunda)

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)
"""


# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista  # copia

print(nova)

nova.append(4)

print(lista)
print(nova)


