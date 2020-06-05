"""
Bloco With
With -> 'Com'

Passos para se trabalhar com arquivos:
1 - Abrimos o arquivo;
2 - Manipulamos o arquivo;
3 - Fechamos o arquivo;

O bloco With é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco With.

arquivo = open('texto.txt')

"""

# O bloco With - Forma Pythônica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

# print(arquivo.readlines()) -> With fecha o processo após o uso e acontece o ValueError.

print(arquivo.closed)