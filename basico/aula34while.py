"""
AULA 34 - WHILE

*  Utilizado para realizar ações enquanto uma condição for verdadeira;
*  Requisitos: entender condições e operadores.
*  Existem dois modos de fazer repetições em python, o laço 'while' e o laço 'for'.
*  Para utilizar o laço while, utilizamos a palavra 'while', uma condição e uma expressão a ser executada.
Ex: while 'condição':
        print('Alguma coisa')
    O laço 'while', assim como o 'if' terá um bloco de código 'filho', ou seja, um bloco que será executado abaixo,
    dentro da hierarquia.
"""
#   O código irá ficar repetindo infinitamente o código abaixo, pois a condição foi fixada como 'True'.
# while True:
#     nome = input('Qual o seu nome?: ')
#     print(f'Olá, {nome}.')

#   Um bloco que conte de 0 a 10

# x = 0            #  'X' foi definido como zero, porém será redefinido após o print de 'X', sempre adicionando +1.
# while x < 10:    # enquanto 'X' for menor que zero...
#     print(x)     # ...imprima 'x'
#     x += 1       # X será somado com 1 e substiruirá o valor da variável 'X'.
                 # será mostrado até o número 9 no console, pois quando 'X' for igual a dez, o resultado de 'while'
                 # mudará para 'False' e encerrará o loop. While checa se 'X' é menor que '10' e nesse momento ele será
                 # igual a '10'.
# print('Acabou!') # Quando a expressão checar em 'False', o interpretador irá saltar a hierarquia dentro de 'while' e
                 # executará este print, pois ele é o próximo bloco de código fora da hierarquia 'while'.

#   A palavra 'continue serve para reiniciar o laço. Sempre que o interpretador se deparar com ele, ele retorna ao início do laço'
#   Ex:
# x = 0
# while x < 5:
#     continue     #  Quando chegar nesta parte, o interpretador retorna ao início do 'while' executando o próximo laço...
#
#     print(x)     #   ...e esta parte não será executada.
#     x += 1
# print('Acabou!')

#   Como saltar algum número na sequencia de impressão.

# x = 0
#
# while x < 5:
#
#     if x == 3:      #   Quando 'X' for igual a '3', o bloco print não será executado, mas sim o código que estiver dentro
                      #   da hierarquia, que neste caso vai somar x = 1 e  transformar-lo em '4' e não vai imprimir o '3'.
        # x += 1
        # continue
    #
    # print(x)
    # x += 1
#
# print('Acabou!')

#  Similar a 'continue', nós temos o 'break'. Quando o interpretador a encontrar ele irá finalizar o loop e saltará para
#  a próxima linha que estiver fora da hierarquia do loop.

# x = 0
#
# while x < 5:
#     if x == 3:      #  Assim que 'x' for igual a '3', o interpretador finaliza o laço e salta para a próxima linha fora
                      #  dessa hierarquia, no caso, o print 'acabou!'
        # x += 1
        # break
    # print(x)
    # x += 1
# print('Acabou!')

#   Exemplo de MATRIZ.

# y = 0
# x = 0
#
# while x < 6:
#     y = 0
#
#     while y < 6:
#         print(f'({x},{y})')
#         y += 1
#
#     x += 1
#
# print('Finished!')

#   Calculadora com While.

while True:
    num_1 = input('Digite um num.: ')
    num_2 = input('Digite outro num.: ')
    op = input('Dig. um operador: ')


    if not num_1.isdigit() or not num_2.isdigit():
        print('Digite um número válido!!!')
    else:
        num_1 = int(num_1)
        num_2 = int(num_2)

    if op == '+':
        print(num_1 + num_2)
        break
    elif op == '-':
        print(num_1 - num_2)
        break
    elif op == '/':
        print(num_1 / num_2)
        break
    elif op == '*':
        print(num_1 * num_2)
        break

    else:

        print('')
        print('Operador Inválido!!!')