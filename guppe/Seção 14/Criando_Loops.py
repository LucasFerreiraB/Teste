"""
Criando sua propria versão de Loops

for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Luck'
    print(letra)

iter([1, 2, 3, 4, 5])

iter('Luck')
"""

def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('Luck')

numeros = [1, 2, 3, 4, 5]

meu_for(numeros)