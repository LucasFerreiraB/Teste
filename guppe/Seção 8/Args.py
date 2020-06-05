"""
Entendendo o *Args

- O args é um parametro, como outro qualquer, Isso significa que voce poderá chamar de qualquer coisa, desde que começe
com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args?
O parametro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Então desde já
lembre-se que tuplas são imutáveis.

# Exemplos

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 5, 9))


# print(soma_todos_numeros(3, 4))  TypeERROR

# Entendendo o args

def soma_todos_numeros(nome, email, *args):
    return sum(args)

 #total = 0
    #for numero in args:
        #total = total + numero
    #return total


print(soma_todos_numeros('Lucas', 'Luck'))
print(soma_todos_numeros('Lucas', 'Luck', 1))
print(soma_todos_numeros('Lucas', 'Luck', 2, 3))
print(soma_todos_numeros('Lucas', 'Luck', 2, 3, 4))
print(soma_todos_numeros('Lucas', 'Luck', 3, 4, 5, 6))

# Outro exemplo de utilização de *args

def verifica_info(*args):
    if 'Luck' in args and 'Ferreira' in args:
        return 'Bem vindo Luck'
    return 'Nao tenho certeza de quem seja você'


print(verifica_info())
print(verifica_info(1, True, 'Ferreira', 'Luck'))
print(verifica_info(1, 'Ferreira', 3.450))

def soma_todos_numeros(*args):
    return sum(args)

# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

num1, num2, num3, num4, num5, num6, num7 = numeros

# Desempacotador

# print(soma_todos_numeros(num1, num2, num3, num4, num5, num6, num7))

print(soma_todos_numeros(*numeros))

# OBS: o asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados
# desta forma, ele saberá que precisará antes desempacotar estes dados.
"""

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

num1, num2, num3, num4, num5, num6, num7 = numeros


print(soma_todos_numeros(num1, num2, num3, num4, num5, num6, num7))

print(soma_todos_numeros(*numeros))