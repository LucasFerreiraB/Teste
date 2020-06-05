"""
Funções com parametros padrões (Default Paranters)

- Funções onde a passagem de parametro
 seja opcional;

# Exemplo de função onde a passagem de parametro seja opcional
print("Luuck")

print()


#Exemplo de função onde a passagem de parametro seja obrigatoria;
def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print(quadrado()) # Type error

def exponencial(numero=4, potencial=2):
    return numero ** potencial


print(exponencial(2, 3)) # 2 * 2 * 2 = 8
print(exponencial(3, 2)) # 3 * 3 = 9

print(exponencial(3))   # Por padrão eleve ao quadrado
print(exponencial(3, 5))   # eleva a potencia informada pelo usuario

# OBS
# Se o usuario passar somente 1 parametro, este será atribuido ao parametro numero, e será calculado o quadrado deste
# número;
# Se o usuario passar 2 argumentos, o primeiro sera atribuido ao parametro numero e o segundo ao parametro potencia, entao
#sera calculada esta potencia.

print(exponencial())

# OBS: em funções python os parametros com valores default (padrao) DEVEM sempre estar ao final da declaração.

# ERRO!
def teste(potencial, num=2):
    return num ** potencial

print(teste(6))

# Outros exemplos

def soma(num1=5, num2=3):
    return num1 + num2

print(soma(4, 3))
print(soma(4)) # type error
print(soma()) # type error

# Exemplo mais complexo

def mostra_informacao(nome='Luck', instrutor=False):
    if nome == 'Luck' and instrutor:
        return 'Bem vindo instrutor Luck'
    elif nome == 'Luck':
        return 'Eu pensei que voce era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True)) # SÓ True, irá passar para o primeiro parametro
print(mostra_informacao('Ferreira'))
print(mostra_informacao(nome='Lucas'))

# Por que utilizar parametros com valor default?
- Nos permite ser mais flexiveis nas funções;
- Evita erros com parametros incorretos;
- Nos permite trabalhar com exemplos mais legiveis de códigos;

# Quais tipos de dados podemos utilizar como valores default (valores padrões) para parametros?
- Qualquer tipo de dado:
    - Numeros, string, floats, booleanos, listas, tuplas, dicionarios, funções e etc;

# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# escopo - evitar problemas e confusões...

# variaveis globais
# vairaveis locais

instrutor = 'Luck' # variavel global

def diz_oi():
    instrutor = 'Python' # variavel local
    return f'Oi {instrutor}'


print(diz_oi())

# OBS: Se tivermos uma variavel local com o mesmo nome de uma variavel global, a local terá preferencia.

def diz_oi():
    prof = 'Geek' # variavel local
    return f'Olá {prof}'

print(diz_oi())

print(prof) # Name error

# Atenção com variaveis globais, se puder evite.

total = 0


def incrementa():
    global total  # avisando que queremos utilizar a variavel global

    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variavel (não é comum)

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())

print(dentro) # NameError
"""

def mostra_informacao(nome='Luck', instrutor=False):
    if nome == 'Luck' and instrutor:
        return 'Bem vindo instrutor Luck'
    elif nome == 'Luck':
        return 'Eu pensei que voce era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True)) # SÓ True, irá passar para o primeiro parametro
print(mostra_informacao('Ferreira'))
print(mostra_informacao(nome='Lucas'))


