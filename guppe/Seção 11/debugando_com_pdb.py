"""
Debugando com PDB

PDB -> Python Debugger, ou seja remover o buggger.

Bug -> Inseto


# OBS: a utilização do print() para debugar código é uma prática ruim.
def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger. Em python, podemos fazer isso em diferentes IDEs
# como em Pycharm ou utilizando o PDB - Python Debugger

# Exemplo com o PyCharm

# OBS: a utilização do print() para debugar código é uma prática ruim.
def dividir(a, b):
    #print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 0))

# Exemplo com PDB - Python Debugger - Exemplo 1

# Para utilizar o Python Debugger, precisamos importar a biblioteca pbd e então utilizar a função set_trace()
# Comandos básicos do PDB:
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variavel)
# c (continua a execução - finaliza o debugging)

import pdb

nome = 'Lucas'
sobrenome = 'Fer'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo com PDB - Python Debugger - Exemplo 2

# Para utilizar o Python Debugger, precisamos importar a biblioteca pbd e então utilizar a função set_trace()
# Comandos básicos do PDB:
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variavel)
# c (continua a execução - finaliza o debugging)

nome = 'Lucas'
sobrenome = 'Fer'
import pdb; pdb.set_trace() # Para executar dois comandos na mesma linha, usa-se ";"
nome_completo = nome + ' ' + sobrenome
curso = 'Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Porque utilizar este formato?
# O Debugger é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas no inicio do arquivo.
# Por isso ao invés de colocarmos o import do pdb no inicio do arquivo, nós colocamos somente onde vamos debuggar, e ao finalizar
# já fazemos a remoção.

# Exemplo com PDB - Python Debugger - Exemplo 3

# Para utilizar o Python Debugger, precisamos importar a biblioteca pbd e então utilizar a função set_trace()
# * A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando do debug foi incorporado como função built-in (integrada)
# chamada breakpoint()
# Comandos básicos do PDB:
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variavel)
# c (continua a execução - finaliza o debugging)

nome = 'Lucas'
sobrenome = 'Fer'
# import pdb; pdb.set_trace() # Para executar dois comandos na mesma linha, usa-se ";"
breakpoint()  # Usamos este comando ao inves do import de cima a partir da versão 3.0 de Python
nome_completo = nome + ' ' + sobrenome
curso = 'Python'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""


# OBS: Cuidado com confiltos entre nomes de variáveis e os comandos do pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))

# Como os nomes das variáveis são os mesmos dos comandos pdb, devemos utilizar o comando p para imprimir as variáveis, ou seja: p nome_da_variavel
# Nada de colocar nomes não representativos em variáveis, sempre opitar por nomes significativos.

def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4