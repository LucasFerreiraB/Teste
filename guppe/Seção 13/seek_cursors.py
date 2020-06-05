"""
Seek e Cursors

seek() -> é utilizada para movimentar o cursor pelo arquivo.


arquivo = open('texto.txt')

print(arquivo.read())

# seek() -> A função seek() é utilizada para a movimentação do cursor pelo arquivo. Ela recebe um parametro que indica
# onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek() -> seek = Procurar
arquivo.seek(0)  # seek

print(arquivo.read())

arquivo.seek(20)

print(arquivo.read())



arquivo = open('texto.txt')

#print(arquivo.read())

# readline() -> função que lê o arquivo linha a linha

print(arquivo.readline())

#ret = arquivo.readline()
#print(type(ret))
# print(ret.split(' '))


# readlines()

# print(arquivo.readlines()) # Lê as linhas e transforma em uma lista de String

linhas = arquivo.readlines()

print(len(linhas))

# print(arquivo.readlines()) # Transforma em uma lista de String

# OBS: Quando abrimos um arquivo com a função open()  é criada uma conexão entre o arquivo no disco do computador e o
nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo, devemos fechar essa conexão
para isso, utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;
2 - Trabalhar com o arquivo;
3 - Fechar o arquivo;


# 1 - Abrir o arquivo;
arquivo = open('texto.txt')

# 2 - Trabalhar com o arquivo;
print(arquivo.read())

print(arquivo.closed) # Verifica se o arquivo está aberto ou fechado - Nesse caso 'False'

# 3 - Fechar o arquivo;
arquivo.close()

print(arquivo.closed) # Verifica se o arquivo está aberto ou fechado - Nesse caso 'True'

# print(arquivo.read()) # Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError
"""

arquivo = open('texto.txt')

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(50))