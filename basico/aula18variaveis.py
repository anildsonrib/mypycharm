"""
Características (regras) de uma variável:

* Deve iniciar com uma letra;
* Pode conter números (mas obrigatoriamente deve iniciar com letra);
* Utiliza o sinal de igual como operador de atribuição, ou seja,: nome= 'Anildson' O sinal de igual, atribui a str
   'Anildson' à variável 'nome'
* Usa o sinal de 'underline' para fazer a separação dos caracteres. Ex: 'dataatual =', pode ser separado em 'data_atual =',
   utilizando o "_"
* Utilizar sempre letras minúsculas para criar uma variável.
"""
print('==============')
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
print('==============')

print(nome, 'tem', idade, 'anos de idade, e o  seu imc é de:', int(imc))
print('==============')
