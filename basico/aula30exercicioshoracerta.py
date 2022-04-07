"""
Faça um programa que pergunte a hora ao usuário;
Baseando-se no horário descrito, exiba a saudação apropriada:
Ex: Bom dia de 0-11   Boa tarde de 12 - 17   Boa noite de 18-23
Caso o usuário não digite um valor válido, informe que ele não digitou um valor válido.
"""

hor = input('Digite a hora: ')
min = input('...e os minutos?: ')

if hor.isdigit() and min.isdigit():

    hor = int(hor)
    min = int(min)

    if hor < 0 or hor > 23:
        print(f'Horário deve estar en 0 e 23 horas.')
    elif hor <= 11:
        print(f'Bom dia, são {hor}:{min}h.')
    elif hor <= 17:
        print(f'Boa tarde, são {hor}:{min}h.')
    else:
        print(f'Boa noite, são {hor}:{min}h.')
else:
    print('Você não digitou um valor válido.')