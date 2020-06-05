"""
Estruturas logicas: AND (e), OR (ou), NOT (nao), IS (é)

Operadores unarios:
    - not, is
Operadores binarios:
    - and, or

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja se for True, vira False se for False vira True
Para o 'is', o valor é comparado com um segundo,
"""

"""
# Se não estiver ativo
if not ativo:
    print('voce precisa ativar sua conta, por favor cheque seu e-mail')
else:
    print('Bem vindo')
    
    
"""

ativo = True
logado = False

if ativo:
    print('Bem vindo')
else:
    print('voce precisa ativar')

# ativo é True?
print(ativo is True)

#  print(not False)
"""
if ativo or logado:
    print('Bem vindo Usuario')
else:
    print('voce precisa ativer sua conta. Por favor, cheque seu e-mail')
"""