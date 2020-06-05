"""
Escrevendo em arquivos

OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler.
Da mesma forma, se abrirmos um arquivo, não podemos lê-lo, somente escrever nele.

OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir um arquivo utilizamos a função write().
Esta função recebe uma String como parâmetro. Caso contrário teremos TypeError.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado, caso ele já exista, o anterior será
apagado e um novo será criado. Dessa forma, todo o conteúdo no arquivo anterior é perdido.


# Exemplo de scrita - modo 'w' -> write (escrever)

# Forma pythônica:

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados. \n')
    arquivo.write('Outros Podemos colocar tudo. \n')
    arquivo.write('Mais Essa é a ultima linha. \n')


# Forma tradicional de escrita em arquivos -> Não pythônica:

arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer. \n')
arquivo.write('Mais um texto. \n')

arquivo.close()


with open('luck.txt', 'w') as arquivo:
    arquivo.write('Lucas. \n' * 1000)
"""

with open('Frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break



