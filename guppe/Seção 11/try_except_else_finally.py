"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

Toda entrada deve ser tratada !!

OBS: A função do usuário é DESTRUIR seu sistema.

# num = 0
# Else -> só é executado somente se não ocorrer o erro.

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Voce digitou {num}')

# Finally
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Voce não digitou um valor válido. ')
else:
    print(f'Voce digitou o número {num}')
# print('Depois do bloco try/except ')
finally:  # O Finally funciona da mesma forma que o print de cima.
    print('Executando o finally')

# OBS: O bloco Finally é SEMPRE executado, independente se houve exceção ou não.

# O finally geralmente é usado para fechar ou deslocar recursos.


# Exemplo mais complexo ERRADO

def dividir(a, b):
    return a / b

num1 = int(input('Informe o primeiro numero: '))
try:
    num2 = int(input('Informe o segundo numero: '))
except ValueError:
    print('O valor precisar ser numérico')
try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')


# Exemplo mais complexo CORRETO
# Você é responsável pelas entradas das suas funções, então, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por "0" '

num1 = input('Informe o primeiro numero: ')
# num1 = int(input('Informe o primeiro numero: '))
num2 = input('Informe o segundo numero: ')
# num2 = int(input('Informe o segundo numero: '))

print(dividir(num1, num2))


# Exemplo mais complexo CORRETO - Genérico
def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'

num1 = input('Informe o primeiro numero: ')
# num1 = int(input('Informe o primeiro numero: '))
num2 = input('Informe o segundo numero: ')
# num2 = int(input('Informe o segundo numero: '))

print(dividir(num1, num2))
"""

# Exemplo mais complexo CORRETO - Semi Genérico
# Você é responsável pelas entradas das suas funções, então, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

num1 = input('Informe o primeiro numero: ')
# num1 = int(input('Informe o primeiro numero: '))
num2 = input('Informe o segundo numero: ')
# num2 = int(input('Informe o segundo numero: '))

print(dividir(num1, num2))


