
print(15 * '=')  # operador multiplicando uma str
nome = 'Anildson'
idade = 37  # int
altura = 1.75  # float
peso = 90.0  # float
e_maior = idade > 18  # bool
data_atual = 2019  # int
imc = peso / altura ** 2

print('Nome:', nome)
print('Idade:', idade, 'Anos')
print('Altura:', altura, 'M')
print('Peso:', peso, 'Kg')
print('É maior de idade?', e_maior)
print(15 * '=')  # operador multiplicando uma str
print(nome, 'tem', idade, 'anos de idade, e o  seu imc é de:', (imc))
print(f'{nome} tem {idade} anos de idade, e o seu imc é de: {imc:.2f}')
# Essa linha foi formatada usando a função f' que retirou a necessidade de colocar aspas
# simples nas str e as vírgulas separando os elementos dentro da linha do código. Porém
# todas as variáveis foram colocadas dentro de chaves. Na variável imc, colocou-se o código
# ":.2f" para definir apenas duas casas decimais após a virgula.
print('{} tem {} anos de idade, e o seu imc é de: {:.3f}'.format(nome, idade, imc))
print(55 * '*')  # operador multiplicando uma str
