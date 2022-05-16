"""


                                  AULA 41 - Split, Join, Enumerate em python

------------------------------------------------------------------------------------------------------------------------

* Split
        :(dividir uma string): O método Python split é uma das funções disponíveis em Python utilizada para a
        manipulação de strings. Na prática, ele permite dividir o conteúdo da variável de acordo com as condições
        especificadas em cada parâmetro da função ou com os valores predefinidos por padrão. A função split te permite
        dividir uma string e gerar uma lista.

Ex:
string = "O brasil é o país do futebol, o Brasil é penta"
lista = string.split(' ') # 'lista' vai receber o resultado da separação da variável 'string' que foi feita pela função
                             split. Entre parenteses foi definido que a divisão ocorreria entre cada espaço entre as
                             palavras, ou seja, toda vez que o código encontrava um espaço, ele separava a palavra e a
                             adicionava à um índice na variavel 'lista'.

print(lista) R: ['O', 'brasil', 'é', 'o', 'país', 'do', 'futebol,', 'o', 'Brasil', 'é', 'penta']

    A sintaxe de split: 'variável a ser separada'.split('parametro de separação')
                                                  string.split(' ')
------------------------------------------------------------------------------------------------------------------------
* Join (juntar uma lista)
* Enumerate (enumerar elementos de uma lista)

------------------------------------------------------------------------------------------------------------------------

* Count
         :A função count() retorna a quantidade de vezes que um mesmo elemento está contido numa lista. Essa é uma excelente
    maneira que evita a implementação de um Laço de Repetição em busca de elementos iguais.

Ex:
texto = 'três pratos de trigo para três tigres tristes, três menos três é igual a um'
lista = texto.split(' ') # Transformamos todos os valores da var 'texto' em uma lista, utilizando a função split com o
                           parametro de separação por espaços entre as palavras.

contagem = lista.count('três') # Com a função ".count()" pedimos para que seja contada quantas vezes o valor 'três'
                                 aparece dentro da lista. Entre os parenteses nós colocamos o valor a ser contado
print(contagem) # R: 4

------------------------------------------------------------------------------------------------------------------------
Strip:
        O método strip () retorna uma cópia da string removendo os caracteres iniciais e finais (com base no argumento
        da string passado). O strip() método remove os caracteres da esquerda e da direita com base no argumento (uma
        string que especifica o conjunto de caracteres a ser removido).


"""
#======================================================================================================================

# SPLIT:
# Divida os elementos de uma frase (palavras) com a função split, e crie uma lista com esses elementos.

string = 'O brasil é o país do futebol, o Brasil é penta'
lista = string.split(' ')
print(lista)
print('')

# R: ['O', 'brasil', 'é', 'o', 'país', 'do', 'futebol,', 'o', 'Brasil', 'é', 'penta']

#======================================================================================================================

# SPLIT:
# Utillizando como parâmetro a vírgula, divida uma frase e a transforme em uma lista, com a função split.

string = 'O brasil é o país do futebol, o Brasil é penta'
lista_2 = string.split(',')
print(lista_2)
print('')
# R: ['O brasil é o país do futebol', ' o Brasil é penta']
#======================================================================================================================

# COUNT:
# Crie um código que itere em uma determinada frase e mostre o resultado de quantas vezes cada palavra aparece na frase:

frase = 'O brasil é o país do futebol, o Brasil é penta'
lista = frase.split(' ')
for valor in lista:
    print(f'A palavra "{valor}" apareceu {lista.count(valor)}x na frase.')
print('')
# R: A palavra "O" apareceu 1x na frase.
#    A palavra "brasil" apareceu 1x na frase.
#    A palavra "é" apareceu 2x na frase.
#    A palavra "o" apareceu 2x na frase.
#    A palavra "país" apareceu 1x na frase.
#    A palavra "do" apareceu 1x na frase.
#    A palavra "futebol," apareceu 1x na frase.
#    A palavra "o" apareceu 2x na frase.
#    A palavra "Brasil" apareceu 1x na frase.
#    A palavra "é" apareceu 2x na frase.
#    A palavra "penta" apareceu 1x na frase.

#======================================================================================================================

# COUNT:
# Crie um código que retorne qual foi a palavra mais vezes apareceu dentro de uma frase:

texto = 'três pratos de trigo para uns três tigres tristes, uns uns três menos um é uns igual a uns dois, uns'
lista = texto.split(' ')
palavra = ''
contagem = 0

for valor in lista:
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x).')

# R: A palavra que apareceu mais vezes é uns (6x).

#======================================================================================================================
