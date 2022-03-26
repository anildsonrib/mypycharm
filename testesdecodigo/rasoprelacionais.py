"""
print(2 == 2)
print(2 == '2')

num_1 = 2
num_2 = 2
expressão = num_1 == num_2
print(expressão)

num_1 = 2
num_2 = 2
print(num_1 > num_2)

var_1 = 'anildson'
var_2 = 'anildson'
expressão = var_1 != var_2

print(expressão)
"""

nome = input('Digite o seu nome: ')
idade = int(input('Qual a sua idade?: '))
id_limite = 18

if idade >= id_limite:
    print(f'{nome} está apto para o empréstimo.')
else:
    print(f'{nome} NÃO está apto.')