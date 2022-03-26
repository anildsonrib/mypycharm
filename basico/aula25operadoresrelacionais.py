"""
 *OPERADORES ***RELACIONAIS***: São utilizados para fazer comparações de elementos dentro do código;
 *Sempre que um operador for executado, ele sempre retornará um valor 'boolean' (true or false)

 == Igual *Ele pergunta se um item é igual a outro. ('=' é utilizado para afirmar categoricamente que um item é igual ao outro)
 >  Maior que...
 >= Maior ou iguala a...
 <  Menor que...
 <= Menor ou igual a...
 != Diferente de...
"""
# Criar um código para verificar se um usuário está apto a conseguir um empréstimo.
# Definir que a idade para os aptos deve ser maior ou igual a 18 anos.

# Passo a Passo:
#    *criar uma variável com um 'input' perguntando o nome do usuário
#    *criar uma nova variável com um 'unput' perguntando a idade do usuário
#    *fazer a comparação entre a idade do usuário e a idade limite para poder pegar o empréstimo
#    *imprimir o resultado dizendo se o usuario foi ou não aprovado para fazer o empréstimo//

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
idade_menor = 18
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome}, você pode pegar o empréstimo.')
else:
    print(f'{nome}, você NÃO pode pegar o empréstimo')
