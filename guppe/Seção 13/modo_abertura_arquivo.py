"""
Modo de abertura de arquivo

r - abre para leitura - padrão
w - abre para escrita - sobrescreve caso o arquivo já exista
x - abre para escrita - somente se o arquivo não existir. Caso o arquivo exista, gera FileExistError
a - abre para escrita - adicionando o conteúdo ao final do arquivo.
+ - bare para o modo de atualização: Leitura e Escrita. (Temos o controle do cursor)

OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo será adicionado ao
final do arquivo SEMPRE. Com o modo 'a' não controlamos o cursor,

http://docs.python.org/3/library/functions.html#oExepen

# Exemplo x
try:
    with open ('udf.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo.\n')
except FileExistsError:
    print('Arquivo já existe')

# Exemplo a
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma frutra ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

# Exemplo r+
with open('outro.txt', 'r+') as arquivo:
    arquivo.write('Adicionando \n')
    arquivo.seek(11)
    arquivo.write('No topo!!! \n')
    arquivo.seek(32)
    arquivo.write('Mais uma linha. \n')
"""


