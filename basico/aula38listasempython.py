"""
Listas em python

"Lista", é um tipo de dado em python que pode armazenar vários valores nela. Similar a ela, nós temos a 'variável' que
armazena apenas um dado. Ex:

nome = 'Anildson' #variável
nomes = ['Anildson', 'novembro', True, 10, 8.5] #lista

Uma lista será criada entre colchetes [].
Os elementos (valores) dentro de uma lista, são posicionados linearmente, e estas posições são chamadas de índices. Para
acessar os valores dentro de uma lista, utilizaremos os índices. Ex:

          0    1     2     3    4     # índices
lista = ['A,  'B',  'C',  'D', 'E']   # valores
         -5    -4   -3    -2   -1     # índices negativos

Podemos modificar um valor dentro de uma lista, ou seja, podemos substituí-lo por qualquer outra coisa.
Ex: Na lista abaixo, para modificarmos o valor do índice '5', criamos uma outra variável especificando  o índice a ser
alterado e atribuímos qualquer outro valor que quisermos à ele.
Ex:
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
lista[5] = 'changed'

print(lista)
R: ['A', 'B', 'C', 'D', 'E', 'changed']
#______________________________________________________________________________________________________________________

A lista, assim como as variáveis strings, também permitem o fatiamento.
Ex: Para exibir apenas os índices 1, 3, 5, nós colocaremos entre colchetes os seguintes dados [0:6:2], ou seja, inicia
no 0, vai até o 6 e pula de dois em dois. start /stop /step

lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[0:6:2])
R: [A, C, E]

#______________________________________________________________________________________________________________________

* A função 'extend', mescla duas listas, fazendo com que passe a existir apenas uma, com todos os elementos.
Ex:
l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
l1.extend(l_2)                          # momento em que a lista 1 foi extendida.

print(l_1)  #    R: [1, 2, 3, 4, 5, 6]  # a lista 1, foi extendida com todos os valores da lista 2
print(l2)           [4, 5, 6]           # lista 2 sendo exibida intacta.

#______________________________________________________________________________________________________________________

* A função append insere um registro após o último elemento, ou seja, ele é útil quando é preciso colocar o novo
    registro na última posição da tabela.
Ex:
l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
l1.append('b')

print(l_1)  #    R: [1, 2, 3, 'b']
print(l2)           [4, 5, 6]

#______________________________________________________________________________________________________________________


* Com a função insert, podemos adicionar algum outro dado em qualquer posição que indicarmos dentro da lista:
Ex:
l_1 = [1, 2, 3, 4]
l1.insert(2, 'banana') #    Escolho a lista a ser alterada, coloco um '.insert', abro aspas e digito a posição a ser
                            realocada, digito o novo dado que irá entrar e fecho aspas.

print(l_1)  #    R: [1, 2, 'banana', 3, 4] A função insert inseriu o dado na posição 2 e realocou todos os dados
                    seguintes em novas posições

#______________________________________________________________________________________________________________________

* Afunção '.pop()' irá remover o último indice da lista (caso esse não seja indicado entre parenteses).

Ex:
l_1 = [1, 2, 3, 4]
l1.pop()
print(l1) # R: [1, 2, 3]

#______________________________________________________________________________________________________________________

* A palavra chave 'del' apaga um, ou certo trecho, em uma lista. Pode ser usado como fatiamento para apagar um intervalo
    indicado. Caso não for indicado nenhum intervalo, a palavra chave apagará a lista inteira.
Ex:
l1 = [1,2,3,4,5,6,7,8,9,10]
del(l1[3:8])    #apagou do indice 3 ao indice 7 da lista 'l1'.
print(l1)   #   R: [1, 2, 3, 9, 10]

Ex por fatiamento:
l1 = [1,2,3,4,5,6,7,8,9,10]
del(l1[3:8:2])              # apagar start=3, stop=8, step=2
print(l1)   # R: [1, 2, 3, 5, 7, 9, 10] # foram removidos os indices 3, 5 e 7.

#______________________________________________________________________________________________________________________

* As funções 'min' e 'max' irão iterar em uma lista e retornar o valor que estiver no menor e no maior indice.

Ex:
l1 = [1,2,3,4,5,6]
print(max(l1))
print(min(l1))  # R: 6   # indice '5'
                     1   # indice '0'


#______________________________________________________________________________________________________________________

* A função range sozinha NÃO retorna uma lista, ela retorna um objeto range. Para que a função range retorne uma lista,
    com uma sequencia de números em um intervalo, ela deve ser escrita como um fatiamento (start, stop, step).

Ex:
l1 = range(1, 100)
R: [1, 100] # neste caso, esse seria o retorno da função range.

    O python tem uma função built-in chamado 'list', que converte um objeto iteravel em uma lista.

Ex range() utilizado com 'list':
l1 = list(range(1, 21, 5))      # função 'list' solicitou um range de 1 a 21, pulando de 5 em 5. (start, stop, step)

print(l1)   # R: [0, 5, 10, 15, 20]

Ex de range() utilizado com o laço 'for':
l1 = list(range(0, 21, 5))

for valor in l1:
    print(valor) # R:   0
                        5
                        10
                        15
                        20

#______________________________________________________________________________________________________________________

*fatiamento: Fatiamento (start:stop:step) significa extrair apenas uma parte da string, ou seja, uma substring. Com essa
    operação, podemos delimitar os limites inferior e superior do pedaço da string que queremos acessar.

*append: insere um registro após o último elemento, ou seja, ele é útil quando é preciso colocar o novo registro na
    última posição da tabela.


*insert: O insert é muito parecido com o append. Ele insere um item em uma lista, mas o item inserido vai para a posição
    indicada.

*pop: é uma função embutida no Python que remove e retorna o último valor da lista ou o valor de índice fornecido. Se o
    índice não for fornecido, o último elemento é retirado e removido.

*del: É uma palavra chave que, por fatiamento ([0:6:1]), vai deletar um certo trecho do código. Caso não seja indicado
    o trecho a ser excluido, ele apagará toda a lista.


*clear
*extend:  “Mescla” duas listas, fazendo com que passe a existir apenas uma, com todos os elementos;

*min /max: Essas funções irão me retornar o valor máximo e o mínimo do índice em uma lista.

*range: A função Python range() retorna um conjunto de números sequenciais. Ela contém os parâmetros start, stop e step,
    que permitem configurar o retorno do intervalo de diferentes maneiras, como valores múltiplos de um determinado
    número e até intervalos com números negativos e positivos.

"""
# **********************************************************************************************************************
# **********************************************************************************************************************
# **********************************************************************************************************************


#   Acesse a string 'D' da variável abaixo:

# letras = 'ABCDEFG'
# print(letras[3]) # A0 B1 C2 D3...

# **********************************************************************************************************************

#   Crie uma lista com vários dados e acesse cada um deles com o comando 'print'.

# lista = ['anildson', 10, 'bacana', True]
# print(lista[2])       # R: bacana
# print(lista[0])       # R: anildson
# print(lista[1])       # R: 10
# print(len(lista))     # R: 4      # retornou a quantidade de dados que existem dentro da lista. 4 dados distribuídos
# print(lista[3])       # R: True     do indice 0 ao indice 3.
# print(lista[-1])      # R: True

# **********************************************************************************************************************

#   Utilizando o 'for', acesse cada valor na lista abaixo com o comando print, para que sejam exibidos em linhas
#   diferentes no console.

# lista = ['anildson', 10, 'bacana', True]
# for n in lista:
#     print(n)

# **********************************************************************************************************************

#   Altere o dado do último índice da lista abaixo para 'um texto qualquer':

# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# lista[5] = 'um texto qualquer'
#
# print(lista)
# print(lista[5])     #   Observe que, toda vez que eu acessar o índice '5' em vez de ele apresentar o resultado '10.5',
#   ele apresentará o resultado 'um texto qualquer' pois ele foi alterado na variável seguinte


# **********************************************************************************************************************

# Utilizando o 'fatiamento', crie um código que exiba apenas os dados 'A' 'C' 'E' no console.

# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# print(lista[0:6:2])     #   iniciou no ídice '0' parou no ídice 6 (...mas exibiu o 5º) e saltou de 2 em 2.

# **********************************************************************************************************************

# Reescreva a lista abaixo de modo que exiba os dados de trás para frente.

# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# print(lista[::-1])                      # O duplo 'dois pontos' vazios, quer dizer que ele deve começar do índice 0 até
# o 6, iterando sobre os índices negativos, ou seja, de trás para frente.
# R:[10.5, 'E', 'D', 'C', 'B', 'A']

# **********************************************************************************************************************

# Com a função 'extend', mescle duas listas e exiba o resultado separado de uma delas:

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l1.extend(l2)
#
# print(l1)
# print(l2)
#
#   R: [1, 2, 3, 4, 5, 6] l1 mesclada com l2...
#      [4, 5, 6] ...l2 exibida.

# **********************************************************************************************************************

#   Utilizando a função 'append', crie duas listas e adicione um novo elemento ao final de uma delas.

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l1.append('b')
#
# print(l1)
# print(l2)
#
#  R: [1, 2, 3, 'b']
#      [4, 5, 6]

# **********************************************************************************************************************

# Em uma lista, utilize a função 'insert' para colocar um outro valor no índice 3 desta.

# l1 = [1,2,3,4,5,6]
# l1.insert(3, 'insertado')
#
# print(l1)

#  R: [1, 2, 3, 'insertado', 4, 5, 6]

# **********************************************************************************************************************

# Crie um lista numérica de 0 até 6. Inclua o valor 'inserted' no índice 3 e remova o último item utilizando a função
# 'pop'.

# l1 = [1,2,3,4,5,6]
# print(l1)
# l1.insert(3, 'insert')
# print(l1)
# l1.pop()
# print(l1)

# R: [1, 2, 3, 4, 5, 6]
#    [1, 2, 3, 'insert', 4, 5, 6]
#    [1, 2, 3, 'insert', 4, 5]

# **********************************************************************************************************************

# Em uma lista, apague o seguinte intervalo de índices 3 4 5 6, utilizando a palavra chave 'del':

# l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# del(l1[3:7])
# print(l1)

#       0  1  2  7  8  9   10  11  12
#   R: [1, 2, 3, 8, 9, 10, 11, 12, 13]

# **********************************************************************************************************************

# Escreva uma lista de 1 a 6 e mostre, com o comando print, o maior e o menor indice nesta lista:

# l1 = [1, 2, 3, 4, 5, 6]
#
# print(min(l1))
# print(max(l1))

# **********************************************************************************************************************

# Crie uma lista de numeros de 1 até 20, utlizando um 'range' juntamente com uma função 'list':

# l1 = list(range(1, 21))
# print(l1)

# **********************************************************************************************************************

# Utilizando o laço 'for', escreva um código que exiba os múltiplos de 7, entre 1 e 100.

# l1 = list(range(0, 100, 7))
#
# for m in l1:
#     print(m)

# **********************************************************************************************************************

# Utilizando o laço 'for', escreva um código que exiba a soma de todos os números em um intervalo de 0 a 100.
# Ex: 0+1 = 1+2 = 3+2 = 5+3 = 8+4...

# l1 = list(range(0, 101))
# soma = 0
#
# for valor in l1:
#     soma += valor
# print(soma)

# **********************************************************************************************************************

# Crie uma lista com vários tipos de dados primitivos, e com o laço 'for' itere através deles exibindo o tipo de cada
# um:
# Ex: O tipo de elem é <class 'float'> e o seu valor é -10.5.

# l1 = ['String', True, 10, -20.5]
#
# for elem in l1:
#     print(f'O tipo de "elem" é {type(elem)} e o seu valor é {elem}')

# R: O tipo de "elem" é <class 'str'> e o seu valor é String
#    O tipo de "elem" é <class 'bool'> e o seu valor é True
#    O tipo de "elem" é <class 'int'> e o seu valor é 10
#    O tipo de "elem" é <class 'float'> e o seu valor é -20.5

# **********************************************************************************************************************

