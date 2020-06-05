"""
Sistema de arquivos - Manipulação


# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('arquivo.txt')) # False
print(os.path.exists('frutas.txt')) # True


# Diretório
print(os.path.exists('dir_teste')) # True
print(os.path.exists('outro')) # False
print(os.path.exists('dir_teste/teste')) # True

# Paths absolutos
print(os.path.exists('/Users/lucas/Pictures')) # True
print(os.path.exists('/Users/lucas/Images')) # False


# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass


# Criando arquivos

os.mknod('arquivo-teste4.txt')
os.mknod('/Users/lucas/teste.txt')

# Se o arquivo já existir, teremos o erro FileExistsError

# Criando diretórios

# Path Relativo
os.mkdir('templates')

# Path Absoluto
os.mkdir('/Users/lucas/Pictures/templates')

# Se o diretório já existir, teremos o erro FileExistsError


# Criando multi-diretórios, se já existir FileExistsError
# os.makedirs('P/U/R/P')
os.makedirs('P/U/R/P', exist_ok=True)

# Renomear arquivos e diretórios

os.rename('templates', 'test-temp')

# OBS: Se o diretório não existir teremos um FileNotError, e se não estiver vazio teremos um OSError


# Renomear arquivos e diretórios

# Arquivos
os.rename('dir_teste/teste.txt', 'dir_teste/purp.txt')


# Deletar arquivos

# OBS: Ao deletar um arquivo, eles não vão para a lixeira, somem.
# OBS: Se o arquivo estiver sendo usado e for excluído, dará erro.

# Removendo arquivos
os.remove('arquivo-teste3.txt')

# Deletar diretórios
# Se não estiver vazio teremos um OSError
os.rmdir('test-temp')


# Removendo uma árvore de arquivos
for arquivo in os.scandir('P'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podemos remover uma árvore de diretórios VAZIOS.
# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.
os.removedirs('dir_teste')

# Importando a biblioteca send2trash = Envia arquivos e diretórios para a lixeira.
from send2trash import send2trash

os.remove('novo.txt') # Será deletado sem ir para a lixeira.

send2trash('outro.txt') # Vai para a lixeira. Pode ser restaurado.

send2trash('P') # Diretórios também.
# Se nao existir, dará o OSError.


# Trabalhando com arquivos e diretórios temporários

import os
import  tempfile

# Criando um diretório temporário
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Luck\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando um arquivo para escrevermos um texto. No
# final, usamos um input() só para mantermos os arquivos temporários 'vivos' dentro dos blocos with.

# OBS: possivelmente, o codigo acima não irá funcionar se você estiver utilizando o windows. Por conta desse sistema trabalhar
# de forma diferente com arquivos temporários.

# Criando um arquivo temporário
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Luck\n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos b''


# Sem o bloco with
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Luck\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()



# Trabalhando com arquivos e diretórios temporários

import os
import  tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Luck\n')

print(arquivo.name)

print(arquivo.read())

input()

arquivo.close()

https://docs.python.org/3/library/os.html?highlight=os#module-os
"""
