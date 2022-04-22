"""
Listas em python

"Lista", é um tipo de dado em python que pode armazenar vários valores nela. Similar a ela, nós temos a 'variável' que
armazena apenas um dado. Ex:

nome = 'Anildson' #variável
nomes = ['Anildson', 'novembro', True, 10, 8.5] #lista

Uma lista será criada entre colchetes [].
Os elementos (valores) dentro de uma lista, são chamados de índices. Para acessar os valores dentro de uma lista,
utilizaremos os índices. Ex:
          0    1     2     3    4     # índices
lista = ['A,  'B',  'C',  'D', 'E']   # valores
         -5    -4   -3    -2   -1     # valores negativos

Podemos modificar um valor dentro de uma lista, ou seja, podemos substituí-lo por qualquer outra coisa.
Ex: Na lista abaixo, para modificarmos o valor do índice '5', criamos uma outra variável especificando  o índice a ser
alterado e atribuímos qualquer outro valor que quisermos à ele.
Ex:
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
lista[5] = 'um texto qualquer'

print(lista)
R: ['A', 'B', 'C', 'D', 'E', 'um texto qualquer']

A lista, assim como as variáveis strings, também permitem o fatiamento.
Ex: Para exibir apenas os índices 1, 3, 5, nós colocaremos entre colchetes os seguintes dados [0:6:2], ou seja, inicia
no 0, vai até o 6 e pula de dois em dois.

lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[0:6:2])
R: [A, C, E]



*fatiamento
*append
*insert
*pop
*del
*clear
*extend
*min /max
*range

"""
#************************************************

#   Acesse a string 'D' da variável abaixo:

# letras = 'ABCDEFG'
# print(letras[3]) # A0 B1 C2 D3...

#************************************************

#   Crie uma lista com vários dados e acesse cada um deles com o comando 'print'.

# lista = ['anildson', 10, 'bacana', True]
# print(lista[2])       # R: bacana
# print(lista[0])       # R: anildson
# print(lista[1])       # R: 10
# print(len(lista))     # R: 4
# print(lista[3])       # R: True
# print(lista[-1])      # R: True

#************************************************

#   Utilizando o 'for', acesse cada valor na lista abaixo com o comando print, para que sejam exibidos em linhas
#   diferentes no console.

# lista = ['anildson', 10, 'bacana', True]
# for n in lista:
#     print(n)

#************************************************

#   Altere o dado do último índice da lista abaixo para 'um texto qualquer':

# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# lista[5] = 'um texto qualquer'
#
# print(lista)
# print(lista[5])     #   Observe que, toda vez que eu acessar o índice '5' em vez de ele apresentar o resultado '10.5',
                      # ele apresentará o resultado 'um texto qualquer' pois ele foi alterado na variável seguinte


#************************************************

# Utilizando o fatiamento, crie um código que exiba apenas os dados 'A' 'C' 'E' no console.

# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# print(lista[0:6:2])     #   iniciou no ídice '0' parou no ídice 6 (...mas exibiu o 5º) e saltou de 2 em 2.

#************************************************
