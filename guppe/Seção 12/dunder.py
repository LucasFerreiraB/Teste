"""
Dunder Name e Dunder Main

Dunder -> Double Under

Dunder Name -> __name__

Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos, propiedades e etc utilizando Double Under para não gerar conflito com os
nomes desses elementos na programação.

# Na linguagem C. Temos um programa da seguinte forma:

int main(){
    return 0:
}

# Na linguagem Java, temos um programa da seguinte forma:

public static void main(String[] args){

}

# Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente o Python atribuirá á variável
 __name__ o valor __main__ indicando que este módulo é o módulo de execução principal


from func_com_parametros import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6]))

# OBS: Se um arquivo Pthon for executado diretamente o nome dele será __main__ = Principal, caso o arquivo seja executado via importação
o nome dele será o nome do arquivo.
"""

import primeiro
import segundo
