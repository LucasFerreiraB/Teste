"""
__name__ -> Nome do arquivo executado
__main__ -> Arquivo executado diretamente
"""
def funcao1():
    print('Luck - primeiro.py')

if __name__ == '__main__':  # Essa função faz com que se execute só se for diretamente.
    funcao1()
    print('primeiro.py está sendo executado diretamente')
else:
    print(f'primeiro.py foi importado. {__name__}') # Geralmente não existe esse else.
