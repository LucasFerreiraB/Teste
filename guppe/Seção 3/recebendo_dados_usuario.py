"""
Recebendo dados do usuario

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Lucas'
- Aspas duplas -> "Lucas"
- Aspas simples triplas -> '''Lucas'''
"""
# - Aspas duplas triplas -> """Lucas"""

# Entrada de dados
# print("Qual seu nome?")
# nome = input()  # Input -> Entrada

nome = input('Qual seu nome? \n')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem vindo {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome} \n')

# print("Qual sua idade")
# idade = input()

# idade = input('Qual sua idade? ')

idade = int(input('Qual sua idade? \n'))

# Processamento

# Saida de dados
# Exemplo de print 'antigo' 2.x
# print('O %s Perninha tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'O {nome} tem {idade} anos \n')
"""
int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro. 
"""
# print(f'O {nome} nasceu em {2019 - int(idade)}')
print(f'O {nome} nasceu em {2019 - idade} \n')

