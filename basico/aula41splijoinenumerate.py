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
* Join
       :(juntar uma lista): O método join faz o trabalho inverso do método split. Determinamos um string separador
        (separator), frequentemente chamado de cola (glue) e juntamos os elementos na lista utilizando a cola entre cada
        par de elemento.
Ex:
lista = ["vermelho", "azul", "verde"] # lista a ser colada como uma string;
cola = ';'  # 'glue', valor que irá separar os elementos da string
s = cola.join(lista) # a variavel 's' receberá 'lista' como uma string, separando cada valor com a var 'cola' (;)
print(lista) # R: ["vermelho", "azul", "verde"]
print(s) # R: vermelho;azul;verde


print("***".join(lista))   R: vermelho***azul***verde
print(" ".join(lista))     R: vermelho azul verde
print(","' '.join(lista))  R: vermelho, azul, verde
------------------------------------------------------------------------------------------------------------------------

* Enumerate (enumerar elementos de uma lista)
            : A função enumerate() retorna uma tupla de dois elementos a cada iteração:
              um número sequencial e um item da sequência correspondente. lista, não geram novas listas.
Ex:

texto = "O brasil é penta" # Variável recebendo uma string como argumento.
lista_3 = texto.split(' ') # Função 'split' transforma a 'var' texto em uma lista contendo 4 valores. Utilizou o espaço
                             como critério de divisão

for ind, val in enumerate(lista_3): # A cada iteração na 'lista_3', a função 'enumerate' vai enumerar o índice atual e
                                      atribuir esse valor à variavel 'ind' e atribuir o valor atual na variavel 'val'
    print(ind, val) # R: 0 O
                         1 brasil
                         2 é
                         3 penta

------------------------------------------------------------------------------------------------------------------------

* Count
         :A função count() retorna a quantidade de vezes que um mesmo elemento está contido numa lista. Essa é uma
         excelente maneira que evita a implementação de um Laço de Repetição em busca de elementos iguais.

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

------------------------------------------------------------------------------------------------------------------------
Lista dentro de lista:
                        Em python, é possível colocar uma lista dentro de outra lista.
Ex:
lista = [        # Abre-se um colchete no início, coloca-se quantas listas quiser (cada uma dentro do seu pró´rio colchete,
                   e cada lista separada por virgula) e no fim fecha-se a chave.
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for v in lista:
    print(v[0], v[1], v[2]) # A cada iteração do laço, o console irá mostrar o indice 0, 1 e 2 de cada sublista dentro
                              da lista
R:


"""

#======================================================================================================================
#======================================================================================================================

# SPLIT:
# Divida os elementos de uma frase (palavras) com a função split, e crie uma lista com esses elementos.

string = 'O brasil é o país do futebol, o Brasil é penta'
lista = string.split(' ')
print('Exemplo de "SPLIT": ')
print(lista)
print('')

# R: ['O', 'brasil', 'é', 'o', 'país', 'do', 'futebol,', 'o', 'Brasil', 'é', 'penta']

#======================================================================================================================

# SPLIT:
# Utillizando como parâmetro a vírgula, divida uma frase e a transforme em uma lista, com a função split.

string = 'O brasil é o país do futebol, o Brasil é penta'
lista_2 = string.split(',')
print('Exemplo 2 de "SPLIT": ')
print(lista_2)
print('')
# R: ['O brasil é o país do futebol', ' o Brasil é penta']
#======================================================================================================================

# COUNT:
# Crie um código que itere em uma determinada frase e mostre o resultado de quantas vezes cada palavra aparece na frase:

frase = 'O brasil é o país do futebol, o Brasil é penta'
lista = frase.split(' ')

print('Exemplo de "COUNT": ')
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

print('Exemplo 2 de "COUNT": ')
for valor in lista:
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x).')
print('')

# R: A palavra que apareceu mais vezes é uns (6x).

#======================================================================================================================

# STRIP:
# Na seguinte frase "Penso, logo existo, e se existo, penso então" transforme-a em uma lista com a função 'split',
# utilizando a virgula como parametro de divisão. Imprima cada valor separadamente, eliminando possiveis espaços no
# inicio ou no final de cada valor com a função 'strip'. Os novos valores devem iniciar com letra maiúscula.

frase = "Penso, logo existo, e se existo, penso então"
lista = frase.split(',')

print('Exemplo de "STRIP": ')
for valor in lista:
    print(valor)
    print(valor.strip().capitalize())
print('')

# R:
# Penso
# Penso
#  logo existo
# logo existo
#  e se existo
# e se existo
#  penso então
# penso então

#======================================================================================================================

# JOIN:
# Na lista a seguir "['O', 'brasil', 'é', 'penta']", junte novamente os valores, transformando-os em uma string. Mostre
# os valores na seguinte ordem: * lista original;
#                               * a frase inteira, sem divisões;
#                               * separada por virgulas;
#                               * separadas por um '*'.

string = 'O Brasil é penta'
lista = string.split()

print('Exemplo "JOIN":')
print(lista)
print(' '.join(lista))
print(','.join(lista))
print('*'.join(lista))

print('')

# R: ['O', 'Brasil', 'é', 'penta']
#    O Brasil é penta
#    O,Brasil,é,penta
#    O*Brasil*é*penta

#======================================================================================================================

# ENUMERATE:
# Com o seguinte texto "O brasil é penta", crie um lista e mostre cada um dos seus valores enumerados de acordo com seus
# indices.

texto = "O brasil é penta"
lista_3 = texto.split(' ')

print('Exemplo ENUMERATE: ')
for ind, val in enumerate(lista_3):
    print(ind, val)
print('')

#======================================================================================================================

# Lista dentro de lista:
# Crie uma lista que tenha dentro ela outras 3 sublistas com 3 valores, ([1,2,3], [4,5,6]... até 9). Itere sobre os
# valores destas listas e mostre no console de acordo com cada índide delas.

lista = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print('Exemplo lista dentro de lista:')
for v in lista:
     print(v[0], v[1], v[2])

#======================================================================================================================
