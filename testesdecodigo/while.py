# while True:
#     nome = input('Qual o seu nome?: ')
#     print(f'Olá, {nome}!')

# x = 0
# while x != 10:
#     if x == 3:
#         x = x + 1
#         continue
#
#     print(x)
#     x = x + 1
# print('Acabou!')

# x = 0
# y = 0
#
# while x < 10:
#     print(x)
#     x += 1  #  É a simplificação de "x = x + 1"
# print('Acabou!')

# x = 0
# y = 0
#
# while x <10:
#     y = 0
#     while y < 5:
#         print(f'({x}, {y})')
#         y += 1
#     x += 1
# print('Acabou!')

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    op = input('Digite um operador( + - / *): ')
    sair = input('Deseja sair? [S]im ou [N]ão: ')

    if sair == 's':
        break

    if not num_1.isdigit() or not num_2.isdigit():
        print('Você precisa digitar um número: ')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if op == '+':
        print(num_1 + num_2)
    elif op == '-':
        print(num_1 - num_2)
    elif op == '/':
        print(num_1 / num_2)
    elif op == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido.')