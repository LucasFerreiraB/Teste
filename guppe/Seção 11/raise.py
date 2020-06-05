"""
Levantando os própios erros com raise

raise -> Não é uma função, é uma palavra reservada, assim como def ou qualquer outra em Python

- Lança exceções

Para simplificar, pense no raise como sendo útil para que possamos criar nossas própias exceções e mensagens de erro.

A forma geral de utilização é:

raise TipoError('Mensagem de erro')

# raise ValueError('Valor incorreto')

# Exemplo real:

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma String')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Lucas', 'azul')
# colore('Lucas', 4)
# colore(True, 'azul')

# Exemplo refaturado:

def colore(texto, cor):
    cores = 'verde', 'amarelo', 'azul', 'branco'

    if type(texto) is not str:
        raise TypeError('texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma String')
    if cor not in cores:
        raise ValueError('A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Lucas', 'preto')

OBS: O raise, assim como o return, finaliza a função, Ou seja, nada após o raise é executado.
"""
# Exemplo real:

def colore(texto, cor):
    cores = 'verde', 'amarelo', 'azul', 'branco'

    if type(texto) is not str:
        raise TypeError('texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma String')
    if cor not in cores:
        raise ValueError('A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Lucas', 'preto')
# colore('Lucas', 4)
# colore(True, 'azul')

# OBS: Considere o erro como uma exceção.