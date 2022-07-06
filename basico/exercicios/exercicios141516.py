"""
 1 - PRINT
 Com a função 'print', exiba uma sequencia de numeros no console de 1 a 6:


 R: 123456

=================================================================

 2 - PRINT
 Mostre no console o seu nome completo, como no exemplo: "Anildson de Sousa Ribeiro":

 R: Anildson de Sousa Ribeiro

=================================================================

 3 - SEP

 Utilizando o parâmetro de função 'sep' como argumento nomeado, escreva um código que separe seu nome e sobrenome por vírgulas, asteriscos e barras:

R:
Anildson,Sousa,Ribeiro
Anildson*Sousa*Ribeiro
Anildson/Sousa/Ribeiro

==================================================================

 4 - END

 "Te esperei o dia inteiro "
 "e você não apareceu."

 1 - Mostre no console as frases em linhas separadas (dois prints);
 2 - Mostre no console as frases em linhas separadas (utilizando a quebra de linha);
 3 - Mostre as frases na mesma linha (utilizando dois prints);
 4 - Mostre as frases separadas por vírgula;
 5 - Mostre as frases separadas por barras duplas.

=================================================================

 5 - END E SEP

 "João e maria"
 "correram pelo bosque."

 Utilizando dois prints, exiba essas frases na mesma linha, onde as palavras estão separadas por um traço e as frases separadas por três asteriscos:


=================================================================

 6 - END E SEP: Gerador de CPF.

 Utilizando os parâmetros sep e end, crie um código que exiba este cpf na tela, 824.176.070-18:

=================================================================

7 - CARACTERE DE ESCAPE

 Utilizando o caractere de escape, imprima o seguinte texto: Tudo no mundo real "vai" volta. Inicie o código também com aspas duplas para poder usar o caractere de escape.


R:
Tudo no mundo real "vai" volta.

=================================================================

 8 - TYPE:

 Utilizando a função 'type', mostre no console a classificação dos seguintes dados à seguir:
 "verdura, 10, -12,5, False"



R:
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>


==================================================================

 9 - TYPE:

 Imprima no console o seu nome, sua idade, sua altura e se você é maior de 18 anos, classificando cada tipo de dado utilizando a função 'type'.


R:
Anildson <class 'str'>
37 <class 'int'>
1.75 <class 'float'>
True <class 'bool'>

==================================================================

 10 - OPERADORES

 Escreva um código que exiba os seguintes cálculos abaixo de acordo com esse modelo: Adição: 5 + 3 = "8"

 33+8
 10-17
 9*4
 8/3
 8//3
 8%3
 8**3


R:
Adição: 33 + 8 = "41"
Subtração: 10 - 17 = "-7"
Multiplicação: 9 x 4 = "36"
Divisão: 8 / 3 = "2.6666666666666665"
Divisão inteira: 8 // 3 = "2"
Módulo da divisão: 8 % 3 = "2"
Exponenciação: 8 ** 3 = "512"

==================================================================

 11 - OPERADORES COM STRINGS (concatenação e repetição)

 Utilizando os operadores lógicos "+" e "*", exiba as seguintes informações no console:
Olá mundo!
Olá! Olá! Olá!

R:
Olá mundo!
Olá! Olá! Olá!

==================================================================

12 - PRECEDÊNCIA DE OPERAÇÃO

 Alterando a precedência de operação, escreva um código onde, 2*5-2 = 8, passe a ser igual a 6.


R:
6
"""

print(123456)
print('Anildson de sousa Ribeiro')
print('Anildson', 'Sousa', 'Ribeiro', sep=',')
print('Anildson', 'Sousa', 'Ribeiro', sep='*')
print('Anildson', 'Sousa', 'Ribeiro', sep='/')
print('')
print('Te esperei o dia inteiro ')
print('e você não apareceu.')
print('')
print('Te esperei o dia inteiro \ne você não apareceu')
print('Te esperei o dia inteiro', end=' ')
print('e você não apareceu')
print('Te esperei o dia inteiro', end=', ')
print('e você não apareceu.')
print('Te esperei o dia inteiro', end=' // ')
print('e você não apareceu.')
print('')
print('João', 'e', 'Maria', sep='-', end=' *** ')
print('correram', 'pelo', 'bosque.', sep='-')
print('')
print('824', '176', '070', sep='.', end='-')
print('18')
print('')
print("Tudo no mundo real \"vai\" e volta.")
print('')
print(type('verdura'))
print(type(10))
print(type(-12.5))
print(type(False))
print('')
print('Anildson', type('Anildson'))
print(37, type(37))
print(1.75, type(1.75))
print('É maior de idade?', type(37 > 18))
print('')
print(f'Adição: 5 + 3 = "{5 + 3}"')
print(f'Subtração: 10 - 17 = "{10 - 17}"')
print(f'Multiplicação: 9 * 4 = "{9 * 4}"')
print(f'Divisão: 8 / 3 = "{8 / 3}"')
print(f'Divisão inteira: 8 // 3 = "{8 // 3}"')
print(f'Módulo da divisão: 8 % 3 = "{8 % 3}"')
print(f'Potenciação: 8 ** 3 = "{8 ** 3}"')
print('')
print('Olá ' + 'mundo!')
print('Olá! ' * 3)
print('')
print(2 * (5 - 2))
