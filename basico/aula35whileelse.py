"""
Aula 35 - While /Else
contadores
acumuladores

* O laço 'while' precisa de um número, que no caso é chamado de contador. Esse contador vai garantir que o laço 'while'
terá um fim.
Ex:
contador = 0

while contador =< 10:  # enquanto a 'var' contador for menor ou igual a 10, o código vai imprimir o 'contador' e logo
    print(contador)    # abaixo irá somar +1 a cada vez que ele passar. Assim que o contador chegar a 10, o código para
    contador += 1      # ,,,,,,,,,,,,,,00,2de executar.

* Um contador, vai contando de forma linear, ex: 1, 2, 3, 4, 5, ...
* Um acumulador, é um valor que será somado (incrementado) a cada laço. ex: 1, 2, 4, 8, 16, 32, ...
* No laço 'while', conseguimos usar a expressão 'else'

"""

# contador = 1
# acumulador = 1
#
# while contador <= 10:
#     print(contador, acumulador)
#
#     acumulador += contador
#     contador += 1
# else:
#     print('Cheguei no else.')contador = 1


contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador += contador
    contador += 1
#   O 'else e o 'print', neste caso, farão a mesma função no fim deste código, desde que não haja um 'break' após alguma
#   checagem dentro do código. Se houver um 'break', como na linha 37, o código não executará o bloco do else, mas se
#   houver um print ele o executará. O print não estaria respeitando a hierarquia do bloco 'while', assim como o else
#   está.
else:
    print('Cheguei no else.')
print('O print foi executado.')