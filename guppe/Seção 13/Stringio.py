"""
StringIO

Atenção: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    - Para ler o arquivo.
    - Para escrever o arquivo.

StringIO -> Utilizado para ler e criar arquivos em memória.
"""
# Primeiro fazemos o import
from io import StringIO

mensagem = 'Este é apenas uma string normal \n'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemos utilizar tudo que ja sabemos
print(arquivo.read())

# Escrevendo no arquivo
arquivo.write('Outro texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())