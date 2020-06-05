"""
Utilizando Lambdas

Conhecidas por Expressões lambdas, ou simplismente lambdas, são funções sem nome, ou seja:
funções anônimas.

# Função em Python
def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))

# Expressão  Lambda
lambda x: 3 * x + 1

# Como utilizar a expressão lambda:
calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title() # 'strip' = tira o espaço do inicio e do
fim

print(nome_completo(' Lucas', ' Ferreira'))                                                    # 'title' = Deixa a letra em maiusculo
print(nome_completo(' LUCAS'        , ' ferreira'))



# Em funções Python podemos ter nenhuma ou varias entradas. Em lambdas também

amar = lambda: 'Como não amar Python? '

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x2 ..... xn: <expressão>

print(amar())
print(uma(6))  # OBS: Se passarmos mais parametros ou mais argumentos do que parametros esperados teremos TypeError
print(duas(5, 7))
print(tres(3, 6, 9))

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title() # 'strip' = tira o espaço do inicio e do fim

print(nome_completo(' Lucas', ' Ferreira'))                                                    # 'title' = Deixa a letra em maiusculo
print(nome_completo(' LUCAS'        , ' ferreira'))

#OBS Se passarmos mais argumentos do que parametros esperados teremos TypeError

autores = ['Isac Asimov', 'Ray Brad', 'Robert H', 'Arty C. Clar', 'Frank', 'Orson S C', 'Douglas', 'H. G. Wells', 'Leig Nra']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[0].lower())

print(autores)
"""
# Função Quadrática
# f(x) = a x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    """Retrorna a função f(x) = a*x**2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))