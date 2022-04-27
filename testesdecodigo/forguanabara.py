# for c in range(1, 10, 3):
#     print('oi')

# n = int(input('digite um número: '))
#
# for c in range(0, n+1):
#     print(c)

# i = int(input('Inicio: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
#
# for c in range(i, f+1, p):
#     print(c)

# s = 0
#
# for c in range(1, 5):
#     n = int(input('Digite um valor: '))
#     s += n
# print(f'O somatório total foi {s}')

tab = int(input('Digite uma tabuada que deseja ver: '))
op = input('Digite o operação da tabuada: ')

for dig in range(1, 11):
    if op == '*':
      print(f'{tab} {op} {dig} = {tab * dig}')
    elif op == '/':
      print(f'{tab} {op} {dig} = {tab / dig:.2f}')
