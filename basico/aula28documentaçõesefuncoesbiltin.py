"""
Aula 28 - Documentação e funções built-in úteis

  São funções que fazem checagens das informações fornecidas pelo usuario, evitando que ocorra um erro no seu código.
  Ex: Uma calculadora programada para somar dois números inteiros, se o usuário digitar uma letra em vez de um número,
  programa apresenta um erro e para de funcionar.
  Funções fazem a checagem antecipada das informações a dão outro caminho no código, ou fazem a conversão dessa
  informação.

  isnumeric / isdigit / isdecimal: são funções que checam se uma str pode ser convertida em um número inteiro

***********************************************************************************************************************
#  Ex. 1: Calculadora simples
#  O console solicitará que o usuário digite dois números, e espera-se que retorne o resultado de uma soma, mas o cógigo
#  fará uma concatenação das duas informações, pois o input deu entrada em uma str.
#  2+2=22
num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

print(num_1 + num_2)


#  Ex. 2: Calculadora simples
#  O console solicitará que o usuário digite dois números, e o resultado será da soma desses dois números.
#  O código fez uma typecasting de num_1 e num_2, transformando-os em numeros inteiros.
#  2+2=4
#
num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)

num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

# isnumeric isdigit isdecimal
# Checa se a str tem números positivos
# Após a checagem,  o código retorna um resultado boolean no concole.
print(num_1.isnumeric())
print(num_2.isnumeric())

"""

num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

if num_1.isdigit() and num_2.isdigit(): #  Checa se num1 e num2 são dígitos e se podem ser convertidos para números inteiros.
    num_1 = int(num_1)  #  Se NÃO foi digitado um outro dado que não seja um número inteiro, ele faz a conversão do dado
    num_2 = int(num_2)  #  ...para 'int' tornando possível o cálculo
    print(num_1 + num_2)
#  Se por exemplo, for digitado uma letra quando o console pedir um número, 'isdigit' retornará false, pois não encontrou
#  nenhum dígito e não executará o bloco do código com o cálculo. Então executará o bloco 'else'
else:
    print(f'Não pude converter o dado fornecido para realizar um cálculo')

#  Lembre-se de que "2.2"  "-5" são dígitos, mas são de classes diferentes (float). Para este caso, função 'isdigit' NÃO
#  os considera como aceitáveis para realizar o cálculo.