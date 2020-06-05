"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso codigo.

Os erros mais comuns:

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python não reconhece como parte da
linguagem.

Exemplos SyntaxError

a)

def funcao:
    print('lucas')

b)

None = 1

c)

return

2 - NameError -> Ocorre quando uma variavel ou funcao não foi definida.

Exemplos NameError

a)

print(lucas)

b)

lucas()

c)

a = 18
# msg = 'algo'
if a < 10:
    msg = 'é maior do que 10'

print(msg)

3 - TypeError -> Ocorre quando uma funcao/operação/ação é aplicada a um tipo errado.

Exemplos TypeError:

a)

print(len(6))

b)

print('lucas' + []) # Uma String e uma lista não podem ser concatenadas.

4 - IndexError -> Ocorre quando tentamos acesar um elemento em uma lista ou outro tipo de dado indexado utilizando um indice inválido.

Exemplo IndexError

a)

lista = ['licas']
print(lista[2])

b)

lista = ['licas']
print(lista[0][10])

5 - Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas valor inapropiado.

Exemplos ValueError

a)

# print(int('lucas'))
print(float('lucas'))

6 - KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave que não existe.

Exemplos KeyError:

a)

dic = {'luc': 'Ferreira'}
print(dic['lucas'])

7 - AttributeError -> Ocorre quando uma variavel não tem um atributo/função.

Exemplos AttributeError

a)

# tupla = [11, 2, 43, 4]
tupla = 11, 2, 43, 4
tupla.sort()
print(tupla)

8 - IndentationError -> Ocorre quando nao respeitamos a indentação do Python (4 espaços)

Exemplos IndentationError:

a)

def nova():
print('lucas')

b)

for i in range(10):
i + 1

OBS: Exceptions e Erros são sinonimos na programação.
OBS: Importante ler e prestar atenção na saída de erro.
"""


