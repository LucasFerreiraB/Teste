"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

OBS: Em Python, quando uma função nao retorna nenhuma valor, o retorno é None
OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return
OBS: Não precisamos necessariamente criar uma variavel para receber o retorno de uma função. Podemos passar a execução
de função para outras funções.

# Vamos refatorar (Redifinir) esta função para que ela retorna o valor

def quadrado_de_7():
    return 7 + 7

# Criamos uma variavel para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno {ret}')

print(f'Retorno: {quadrado_de_7()}')

# Refatorando a primeira função
def diz_oi():
    return 'Oi '

alguem = 'pedro'

print(diz_oi() + alguem)

OBS: Sobre a palavra reservada return
1 - Finaliza a função, ou seja, sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores;

# Exemplo 1


def diz_oi():
    print('Executando antes do retorno')
    return 'Oi '
    print('Executando apos o retorno')


print(diz_oi())

# Exemplo 2


def nova_funcao():
    varivael = True
    if varivael:  # Se a variavel for "True" retorna 4
        return 4
    elif varivael is None:
        return 3.2
    else:
        return 'b'


print(nova_funcao())

# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5

# num1, num2, num3, num4 = outra_funcao()
#print(num1, num2, num3, num4)


print(outra_funcao())
print(type(outra_funcao()))

# Criando uma função para jogar uma moeda

from random import random


def joga_moeda():
    #  Gera um numero pseudo-randonico entre 0 e 1
    #  valor = random()
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())
"""
# erros comuns na utilização do retorno de uma função, mas que na verdade nem é erro, mas sim codificação desnecessaria.


def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False


print(eh_impar())


def nova_funcao():
    varivael = True
    if varivael:  # Se a variavel for "True" retorna 4
        return 4
    elif varivael is None:
        return 3.2
    else:
        return 'b'


print(nova_funcao())

