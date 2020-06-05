"""
len, abs, sum e round

# len() -> Retorna o tamanho (ou seja, o numero de itens) de um iteravel.

# Só pra revisar
print(len('Lucas Ferreira'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

# Dunder len - São funções especias.
print('Lucas Ferreira'.__len__())

# abs() -> Retorna o valor absoluto de um numero inteiro ou real. De forma basica, (resumindo) o seu valor real sem o sinal.

# Exemplos Abs

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# print(abs('Lucas')) = TypeError para Strings

# sum() -> Recebe como parametro um iteravel, podendo receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor
inicial.
# OBS: O valor inicial default = 0

# Exemplo Sum

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))

print(sum([3.123, 5.435]))

print(sum((1, 2, 3, 4, 5)))

print(sum({1, 2, 3, 4, 5}))

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

# Round
round() Retorna um numero arredondado para n digito de precisão apos a casa decimal. Se a precisão não for informada retorna o inteiro
mais proximo da entrada.

"""

# Exemplo Round - Retorna um número inteiro ou real ou (arredondado)

print(round(10.2, 3))
print(round(10.2))

print(round(10.5))

print(round(10.6))

print(round(1.2121212121, 2))
print(round(1.2121212121))

print(round(1.21999999, 2))







