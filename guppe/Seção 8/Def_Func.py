"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou nao receber entradas de dados e retornar uma saida de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se voce escrever uma função que realiza varias tarefas dentro dela, é bom fazer uma verificação para que a
função seja simplificada.

Já utilizamos varias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras:

"""
# Exemplo de utilização de funções:

cores = ['verde', 'amarela', 'azul', 'branco']

# Utilizando a função integrada (built-in) do Python print()

# print(cores)

curso = 'Programação em Python: Essencial'
# print(curso)

cores.append('roxo')
# print(cores)

# curso.append('Mais dados...')  # AtributeError
# print(curso)

cores.clear()
# print(cores)

# print(help(print()))

# Dry - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código.

# Mas então, como definir funções?

"""
Em Python, a forma geral de definir uma função é:

def nome_da_função(parametros_de_entrada):
    bloco_da_funcao
    
Onde:

nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto, separado por underline (Snake Case):
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podemos ser opcionais ou nao;
bloco_de_notas -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos 
definindo uma função. Também abrimos o bloco de códigos com o já conhecido dois pontos : que é utilizado em Python 
para definir blocos.    
"""


# Definindo a primeira função
# Definições

def diz_oi():
    print('oi')


"""
OBS: 
1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a unica coisa que ela faz é dizer oi;
3 - Veja que essa função nao recebe nenhum parametro de entrada;
4 - Veja que esta função não retorna nada;
"""

# Utilizando funções
# Chamada de execução

diz_oi()  # Nunca esqueca de utilizar o parentese "()" em executar uma função.


# Exemplo:
# Errado:
# diz_oi

# Certo:
# diz_oi()

# Errado:
# diz_oi ()

# Exemplo 2

def cantar_parabens():
    print('\n')
    print('parabens')
    print('Nesta data')
    print('Muitas felicidades')
    print('anos de vida')
    print('Viva')


# for n in range(5):
#    print(n)
#    cantar_parabens()

# Em Python, podemos inclusive criar variaveis do tipo de uma função e executar esta função atraves da variavel
canta = cantar_parabens

canta()


def rubens_viado():
    print("Rubens viado ao molho.")


gay = rubens_viado

for n in range(10):
    print(n)
    gay()

