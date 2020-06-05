import primeiro

def funcao2():
    primeiro.funcao1()

if __name__ == '__main__':  # Essa função faz com que se execute só se for diretamente.
    funcao2()
    print('segundo.py está sendo executado diretamente.')
else:
    print(f'segundo.py foi importado. {__name__}')  # Geralmente não existe esse else.