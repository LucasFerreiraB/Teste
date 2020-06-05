"""
Documentando funções com Docstrings

OBS: Podemos ter acesso á documentação de uma função em Python
Utilizando a propiedade especial__doc__, exemplo: print(diz_oi,__doc__)
Podemos ainda fazer acesso a documentação com a função help() exemplo: help(diz_oi)

"""

# exemplos
"""def diz_oi():
    """#Uma função simples que retorna a string 'OI!"""
    #return 'Oi!'

# print(diz_oi())
# print(help(diz_oi()))
# print(diz_oi())

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' à 'potencia' informada.
    :param numero: numero que desejamos gerar o exponencial.
    :param potencia: Potencia que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia

print(exponencial(8, 6))