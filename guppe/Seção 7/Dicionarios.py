"""
Dicionarios

Em algumas linguagens de programação, os dicionarios Python são conhecidos por mapas.

Dicionarios são coleções do tipo chave/valor.

Dicionarios são representados por chaves {}

print(type({}))

Sobre dicionario:
    - Chaves e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum)

paises = dict(gay='Thiago', Qualira='Léo', Flavio='Viado')
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informado será retornado o valor None e não será gerado KeyError
pais = paises.get('ru')

if pais:
    print(f'Encontrei o pais {pais}')
else:
    print('Nao encontrei o pais')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o pais {pais}')

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Qualquer tipo de dado pode ser utilizado: (int, string, boolean), inclusive lista, tupla dicionario, como chaves de dicionarios.

# Tuplas são interessantes para se usar como chave de dicionario.

localidades = {
    (35.6895, 39.6917): 'escritorio em Toquio',
    (40.7128, 74.6868): 'escritorio em Nova York',
    (35.7749, 122.4194): 'escritorio em Sao Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - mais comum

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado) # mesma coisa que: receita_update{('mai' : 500)}

print(receita)

# Atualizando dados em um dicionario

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# Conclusao 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma
# Conclusão 2: Não pode ter chaves repetidas.

# Remover dados de um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Aqui precisamos sempre informar a chave e caso nao encontre o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2 - Nesse caso não retorna o valor removido.

del receita['fev']

print(receita)

# Imagine que voce tem um e-comerce, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de compras:
    Produto 1:
        - nome
        - quantidade;
        - preço;
    produto 2:
        - nome
        - quantidade;
        - preço;


# Poderiamos utilizar uma lista para isto? Sim

carrinho = []

produto1 = ['play4', 1, 230.00]
produto2 = ['good of war', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto.

# Forma 2 - Poderiamos utilizar uma tupla para isso? Sim

produto1 = ('Play4', 1, 1.2300)
produto2 = ('good war for', 1, 230.00)

carrinho = (produto1, produto2)

print(carrinho)

# Forma 3 - Poderiamos utilizar um dicionario para isso? Sim
# Forma com melhores informações.
carrinho = []

produto1 = {'nome': 'play4', 'quantidade': 1, 'preco': 230.00}
produto2 = {'nome': 'good', 'quantidade': 1, 'preco': 230.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Metodos de dicionarios;

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionario {zerar dados}

d.clear()

print(d)

# Copiando um dicionario para outro

# Forma 1 - Deep Copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 - Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)
"""
# Forma nao usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'e-mail', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

#  metodo fromkeys recebe dois parametros: um interavel e um valor, ele vai gerar para cada valor do iteravel uma chave e irá atribuir
#  a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

