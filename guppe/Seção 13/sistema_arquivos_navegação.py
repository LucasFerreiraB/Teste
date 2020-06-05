"""
Sistema de arquivos de navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo OS.

OS - Operating System - Sistema Operacional

# getcwd() - pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd()) # C:\Users\lucas\PycharmProjects\guppe\Seção 13

# Para mudar o diretório, podemos utilizando o chdir()

os.chdir('..')

print(os.getcwd()) # C:\Users\lucas\PycharmProjects\guppe

# Podemos se um diretório é absoluto(True) ou relativo(False)

print(os.path.isabs('/Users/lucas')) # True

# OBS: Usuarios windows, Se voce infelizmente estiver usando um computador windows, terá que ter cuidado ao verificar
# diretórios.

print(os.path.isabs('C:\\Users\\lucas'))

# Podemos identificar o sistema operacional com o módulo os
print(os.name) # posix (Linux e Mac), nt (Windows)

# Fazer o import
import os

# Mais detalhes no sistema operacional
print(os.uname())

# Fazer o import
import sys

print(sys.platform)


print(os.getcwd()) # C:\Users\lucas\PycharmProjects\guppe\Seção 13

res = os.path.join(os.getcwd(), 'luck')

os.chdir(res)

print(os.getcwd()) # C:\Users\lucas\PycharmProjects\guppe\Seção 13\luck

# Veja que o os.path.join() recebe dois parametros, sendo o primeiro o diretório atual e o segundo o diretório que será
# juntado ao atual.


# Podemos listar os arquivos e diretórios com o listdir()
print(os.listdir('C:\\'))
"""
import os

# Podemos listar os arquivos e diretórios com mais detalhes com sacndir()
# print(list(os.scandir('C:\\')))

scanner = os.scandir()

arquivo = list(os.scandir())

print(arquivo)

print(dir(arquivo[0]))

print(arquivo[0].inode()) # numeração desse objeto na arvore deste diretório
print(arquivo[0].is_dir()) # è um diretório? False
print(arquivo[0].is_file()) # é um arquivo? True
print(arquivo[0].is_symlink()) # é um link simbólico? False
print(arquivo[0].name) # Nome do arquivo
print(arquivo[0].path) # Caminho até o arquivo
print(arquivo[0].stat()) # estatísticas sobre o arquivo

# OBS: quando utilizamos a função scandir() nós precisamos fecha-lá, assim quando abrimos um arquivo.

scanner.close()

