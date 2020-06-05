"""
Escopo de variaveis

Dois casos de escopo:

1 - Variaveis globais;
    - Variaveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variaveis Locais;
    - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi declarada.

Para declarar variaveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que ao declaramos uma variavel, nós noa colocamos o tipo de dado dela.
Este tipo é inferido ao atribuimos o valor a mesma.

Exemplo em C:
int numero = 42:

Exemplo em Java:
int numero = 42:
"""

numero = 42  # Exemplo de variavel global
print(numero)
print(type(numero))

numero = 'geek'
print(numero)
print(type(numero))

nao_existo = '01'
print(nao_existo)

numero = 42
# novo = 0
if numero > 10:
    novo = numero + 10  # Variavel 'novo' está declarada localmente dentro do bloco do if. Portanto, é local
    print(novo)

print(novo)