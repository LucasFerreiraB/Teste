"""
Funcoes com parametros

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saida

- Não possuem entrada;
- Não possuem saida;
- Possuem entrada mas não possuem saida;
- Não possuem entrada mas não possuem saida;
- Possuem entrada e saida;

# Refatorando uma função:


def quadrado(numero):
   # return numero * numero
   return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

# Refaturando a função:


def cantar_parabens(aniversariante):
   print('Parabens')
   print('Parabens')
   print('Parabens')
   print('Parabens')
   print(f'Viva o {aniversariante}')

cantar_parabens('Lucas')

# Funções podem ter 'n' parametros de entrada, ou seja, podemos receber como entrada em uma função quantos parametros
 forem necessarios. Eles são separados por virgula.

# Exemplo
def soma(a, b):  # Parametro
   return a + b

def multiplica(num1, num2):
   return num1 * num2

def outra(num1, b, msg):
   return (num1 + b) * msg

print(soma(2, 5))  # Argumento
print(soma(10, 20))
print(f'\n')

print(multiplica(2, 5))
print(multiplica(10, 20))
print(f'\n')

print(outra(2, 5, 'Lucas '))
print(outra(10, 20, 'Ferreira '))
print(f'\n')

# OBS: Se a gente informar um numero errado de parametro ou argumentos, teremos TypeError

# Nomeando parametros


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Lucas', 'Ferreira'))

# A diferença entre Parametros e Argumentos

# Parametros são variaveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parametros importa!

nome = 'Lucas'
sobrenome = 'Ferreira'

print(nome_completo(nome, sobrenome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizamos nomes dos parametros nos argumentos para informar-los, podemos utilizar qualquer ordem

print(nome_completo(nome='Lucas', sobrenome='Ferreira'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Ferreira', nome='Lucas'))
"""

# Erro comum na utilização do return

def soma_impares(numeros):
   total = 0
   for num in numeros:
      if num % 2 != 0:
         total = total + num
      #return total = Error
   return total

if __name__ == '__main__':   #OBS: Só executa essa função se executar diretamente.
   lista = [1, 2, 3, 4, 5, 6, 7]
   print(soma_impares(lista))

   tupla = [1, 2, 3, 4, 5, 6, 7]
   print(soma_impares(tupla))






