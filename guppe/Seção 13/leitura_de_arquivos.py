"""
Leitura de arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open().
que literalmente significa 'abrir'. #OBS: open() é uma função integrada

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que neste caso é o caminho para o
arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir ou então teremos o erro FileNotFoundError


        name -> Nome do arquivo // mode='r' -> Modo de abertura, que por padrão é leitura
<_io.TextIOWrapper name='texto.txt mode='r' encoding='UTF-8'> = Variavel arquivo

mode r -> Modo de Leitura. r -> read() -> ler

"""
# Exemplo

arquivo = open('texto.txt')

#print(arquivo)

#print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()
#print(arquivo.read())

ret = arquivo.read()  # Retorna uma String

print(type(ret))

print(ret)


#print(arquivo.read())


# OBS: O Python utiliza um recurso para trabalhar com arquivos chamados cursor. Esse cursor funciona como o cursor quando estamos escrevendo.

#print(arquivo.read()) #OBS: A função read() lê todo o conteúdo de arquivo

#ret = ret.split('\n') -> para trasnformar a String em uma lista e separar as Strings.
