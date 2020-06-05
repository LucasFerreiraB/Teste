"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java

fo(int i = 0; i < 10; i++){
    //execuçção do lop
}
Python

for item in interavel:
    //execução do loop


utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis

Exemplos de iteraveis;
- String
    nome = 'geek universe'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range[1, 10]

# Exemplo de for 1 (iterando em uma String)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando em uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusivo.

for numero in range(1, 10):
    print(numero)
"""


"""
Enumerate:
(0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U'),,,) 

for indice, letra in enumerate(nome):
    print(nome[indice])
    
for indice, letra in enumerate(nome)
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descarta-lá utilizando um underline (_)    

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor[0])

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Geek Univessity'
for letra in nome:
    print(letra, end='')

Tabelas de emojis Unicode: https://apps.timuhitlock.info/emoji/tables/unicode    
"""

# Original: U+1F60D
# Modificado: U0001F60D

for _ in range(3):

    for num in range(1, 11):
        print('\U0001F60D' * num)
