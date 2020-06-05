"""
Modulo Collections - Deque

Podemos dizer que o Deque é uma lista de alto performance.
"""
# Import
from collections import deque

# Criando deques

deq = deque('lucas')

print(deq)

# Adicionando elementos no deque

deq.append('y')  # adiciona no final
print(deq)

deq.appendleft('k')  # adiciona no comeco
print(deq)

# Remover elementos

print(deq.pop())  # Remove o ultimo elemento
print(deq)

print(deq.popleft())
print(deq)
