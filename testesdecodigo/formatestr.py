nome = 'anildson'
idade = 37
altura = 1.75
peso = 90
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade, e o imc é ', imc)
print(f'{nome} tem {idade} anos de idade, e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))


