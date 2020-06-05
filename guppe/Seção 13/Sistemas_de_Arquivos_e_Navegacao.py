"""
Sistemas de arquivos e navegação

Para fazer uso de manipulação do sistema operacional, precisamos importar e fazer uso do módulo OS.

OS -> Operating System - Sistema Operacional


# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd()) # C:\Users\lucas\PycharmProjects\guppe\Seção 13

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')
print(os.getcwd()) # C:\Users\lucas\PycharmProjects\guppe


# Podemos checar se um diretório é absoluto ou relativo

# No linux
print(os.path.isabs('/Users/lucas')) # True (Absolute)

# OBS para usuários windows
Se você, infelizmente, estiver utilizando um computador com windows, terá que ter cuidado ao verificar diretório.

# No windows
print(os.path.isabs('C:\\Users\\lucas')) # True (Absolute)


# Podemos identificar o sistema operacional com o módulo os
print(os.name) # posix (Linux e Mac), nt (Windows)


# Podemos ter mais detalhes no sistema operacional
print(os.uname())


import sys

print(sys.platform)


print(os.getcwd()) # C:/Users/lucas/PycharmProjects/guppe/Seção 13/

res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd()) #C:/Users/lucas/PycharmProjects/guppe/Seção 13/geek/university

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o diretório que será
# juntado ao atual.


# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir())
"""
import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

# print(os.scandir()) # Gera um Iterator Object

scanner = os.scandir()

arquivos = list(scanner)

print(arquivos)

print(dir(arquivos[0]))

print(arquivos[0].name) # Nome do arquivo

print(arquivos[0].inode()) # ??

print(arquivos[0].is_dir()) # É um diretório? False

print(arquivos[0].file()) # É um arquivo? True

print(arquivos[0].symlink()) # É um link simbólico? False

print(arquivos[0].path) # Caminho até o arquivo

print(arquivos[0].stat()) # Estatísticas sobre o arquivo

# OBS: Quando utilizamos a função scandir() nós precisamos fecha-lá, assim quando abrimos um arquivo.

scanner.close()