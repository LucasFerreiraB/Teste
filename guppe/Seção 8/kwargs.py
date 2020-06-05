"""
**kwargs

Poderiamos chamar esse parametro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parametro, mas diferente de *args que coloca os valores extras em uma tupla, o **kwargs exige que
utilizemos parametros nomeados, e transforma esses parametros extras em um dicionário.

# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parametros *args e **kwargs não são obrigatórios.

cores_favoritas()

cores_favoritas(geek='navy')

# Exemplo mais completo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um cumprimento Pythonico Geek'
    elif 'geek' in kwargs:
        return f'{kwargs["geek"]} Geek!'
    return 'Não tenho certeza de quem voce é ...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossas funções, podemos ter (nesta ordem):

- Parametros obrigatórios;
- *args;
- Parametros default (não obrigatórios);
- **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Lucas')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(14, 'Lucas', eu='Não', voce='vai')
minha_funcao(19, 'Lucas', 9, 4, 3, java=False, python=True)

# Entenda por quê é importante manter a ordem dos parametros na declaração


# Função com a ordem correta de parametros
# def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
#    return [a, b, args, instrutor, kwargs]

# Função com a ordem incorreta de parametros
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = ('sobrenome': 'Universidade', 'cargo': 'Instrutor')



print(mostra_info(1, 2, 3, sobrenome='Univesdidade', cargo='instrutor'))
"""

# Desempacotar com kwargs


def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'

print(mostra_nomes(nome='Luck', sobrenome='Ferreira'))

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um cumprimento Pythonico Geek'
    elif 'geek' in kwargs:
        return f'{kwargs["geek"]} Geek!'
    return 'Não tenho certeza de quem voce é ...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Lucas')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(14, 'Lucas', eu='Não', voce='vai')
minha_funcao(19, 'Lucas', 9, 4, 3, java=False, python=True)

