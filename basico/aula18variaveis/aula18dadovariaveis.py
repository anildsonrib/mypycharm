"""


                                  AULA 18 - Variáveis

------------------------------------------------------------------------------------------------------------------------
* Variáveis:
            * Variáveis em Python são lugares reservados na memória de um dispositivo para o armazenamento de dados que
            posteriormente vão ser usados na execução de uma solução digital. Essas variáveis podem ter formatos e
            tamanhos diferentes, entre outras particularidades.
            Para atribuirmos um valor à uma variável, utilizamos o operador de atribuição '=' (sinla de igual), pode ser
            para definir um valor inicial ou para sobrescrever um valor já existente.
            * As regras para a criação de uma variável são:
                •deve iniciar com uma letra;
                •pode conter números;
                •não pode conter espaços, caso precise separar utilizar o underline "_";
                •utliza apenas letras minúsculas (com algumas exceções).

Ex: Criaremos uma variável 'nome' a atribuiremos um valor à ela...

nome = 'Joel' # O valor (str) 'Joel' foi atribuída à variável 'nome' através do operador de atribuição '='.
print(nome)   # A função print exibirá no console  o valor da variável 'nome' (Joel).

            * Podemos realizar operações aritiméticas com variáveis, desde que seus dados permita o cálculo (observar a
            aula de operadores aritiméticos)

Ex:

idade = 32
altura = 1.80

print(idade * altura)

R: 57.6

"""


#======================================================================================================================
#======================================================================================================================

# VARIAVEL

# Crie um variável com o dado (str) 'Arthur' e utilizando a função print exiba o valor dessa variável no console.

nome = 'Arthur'
print(nome)
print('')

#======================================================================================================================

# VARIÁVEL, TYPE

# Utilizando a função type, crie uma variável com o dado (str) 'Arthur', e mostre no console a classificação desse dado.
# R: Arthur <class 'str'>

dado = 'Arthur'
print(dado, type(dado))
print('')

#======================================================================================================================

# VARIÁVEL, PRINT

# Utilizando variáveis, exiba no console as seguintes informações de um usuário: Nome, Idade, Altura, Se é maior de
# idade.
# R: Nome: Pedro
#    Idade: 37
#    Altura: 1.75
#    É maior de idade?: True

nome = 'Pedro'
idade = 37
altura = 1.75
e_maior = idade > 18

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Altura: {altura}')
print(f'É maior de idade?: {e_maior}')
print('')

#======================================================================================================================

# OPERAÇÕES COM VARIÁVEIS

# Utilizando variáveis, exiba no console a multiplicação da altura pela idade de um usuário. Altura, 1.80 /Idade, 32.
# R: 57.6

idade = 32
altura = 1.80

print(altura * idade)
print('')




#======================================================================================================================

# VARIÁVEL, OPERADORES ARITMÉTICOS

# Conforme as informações fornecidas, exiba na tela a seguinte mensagem: André tem 35 anos de idade, e o seu imc é ???.
# (Nome: André, Idade: 35, Altura: 1.90, Peso: 95.3)
# R: André tem 35 de idade, e o seu IMC é 26.40

nome = 'André'
idade = 35
altura = 1.90
peso = 95.3
imc = peso / altura ** 2

print(f'{nome} tem {idade} de idade, e o seu IMC é {imc:.2f}')
print('')

#======================================================================================================================
