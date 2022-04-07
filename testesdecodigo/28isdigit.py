"""
num_1 = input('dig num: ')
num_2 = input('dig outro: ')

print(num_1.isdigit())
print(num_2.isdigit())

num_1 = input('num 1: ')
num_2 = input('num 2: ')

if num_1.isdigit() and num_2.isdigit():

    num_1 = int(num_1)
    num_2 = int(num_2)

    print(num_1 + num_2)
else:
    print('nenhum digito válido.')
"""

num_1 = input('dig num: ')
num_2 = input('dig outro: ')

if num_1.isdigit():
    num_1 = int(num_1)


if not num_1.isdigit():
    print('nehum dig valido')
    elif not num_2.isdigit():
    print('nehum dig valido')
else:
    print(' ')
