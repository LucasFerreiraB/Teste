"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequencias numericas, não de forma aleatoria, mas sim de maneira especificada.

Formas gerais:
range(valor_de_parada)
OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

Formas Gerais;
#Forma 1:

for num in range(11):
    print(num)

#Forma 2:

range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo de 1 em 1)

for num in range(1, 11):
    print(num)

#Forma 3:

range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)

for num in range(5, 55, 5):
    print(num)

#Forma 4 (inverse):

range(valor_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusivo (valor_inicio especificado pelo usuario, e passo especificado pelo usuario)

for num in range(10, -1, -1):
    print(num)
"""
for num in range(5, 55, 5):
    print(num)