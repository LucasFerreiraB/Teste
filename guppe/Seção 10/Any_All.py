"""
Any e All

all() -> retorna True se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel está vazio.

# exemplo all()

print(all([1, 2, 3, 4])) # True
print(all([0, 1, 2, 3, 4])) # False
print(all([])) # True
print(all((1, 2, 3, 4))) # True
print(all({1, 2, 3, 4})) # True
print(all('Lucas')) # True

nomes = ['Cucas', 'Camila', 'Carla', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))

print(all([letra for letra in 'kkk' if letra in 'aeiou'])) # Iterável vazio, portanto 'True'
print(bool([letra for letra in 'kkk' if letra in 'aeiou'])) # Iteravel vazio em Boolean é False

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))
print(bool([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

any() -> Retorna True se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver vazio, retorna False enquanto all() retorna True
"""

print(any([0, 1, 3, 4])) # True
print(any([0, False, {}, (), []])) # False

nomes = ['Cucas', 'Camila', 'Carla', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))

print(all([letra for letra in 'kkk' if letra in 'aeiou'])) # Iterável vazio, portanto 'True'
print(bool([letra for letra in 'kkk' if letra in 'aeiou'])) # Iteravel vazio em Boolean é False

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))
print(bool([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))


nomes = ['Cucas', 'Camila', 'Carla', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))