"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso codigo. Previnindo assim que o programa parar de funcionar e o
usuario receba mensagens de erro inseperado.

A forma geral mais simples é:

try:
    //execução problemática
except:     # Caso você nao consiga, faça isso.
    //o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro genérico

try:
    lucas()
except:
    print('Deu algum problema')

# Tente executar a função lucas(), caso você encontre erros, imprima a mensagem de erro.

# Exemplo 2 - Tratando um erro genérico

try:
    len(5)
except:
    print('Deu algum problema')

OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de forma específica.

# Exemplo 3 - Tratando um erro específico:

try:
    lucas()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 4 - Tratando um erro específico:

try:
    len(5)
except NameError:  # TypeError
    print('Você está utilizando uma função inexistente')

# Exemplo 5 - Tratando um erro específico com detalhes do erro:

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    #print('Lucas' [9])  # IndexError não especificado.
    #len(5)
    lucas()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print(f'Deu um erro diferente')
"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'lucas'}

print(pega_valor(dic, 'nome'))
print(pega_valor(dic, 'game')) # KeyError
print(pega_valor(7, 'nome')) # TypeError


