"""
input('Qual o seu nome?, ')
nome = input('Qual o seu nome?: ')
print(f'O usuário digitou {nome} eu o tipo da variável é '
      f'{type(nome)}')

dado = input('Digite qualquer coisa: ')
print(f'{dado} é {type(dado)}')

nome = input('Digite o seu nome: ')
idade = input('Qual a sua idade?: ')
print('')
print(f'{nome} tem {idade} anos de idade.')

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
ano_nas = 2022 - int(idade)
print(f'{nome} tem {idade} anos. '
      f'{nome} nasceu em {ano_nas}.')

num_1 = input('digite um número: ')
num_2 = input('digite outro número: ')

print(num_1 + num_2)
"""
num_1 = int(input('digite um número: '))
num_2 = int(input('digite outro número: '))

print(num_1 + num_2)
