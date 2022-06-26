"""


                                  AULA 16 - Operadores Aritméticos

------------------------------------------------------------------------------------------------------------------------
Os operadores são usados na construção de expressões, as quais contém um número variado de operandos. Por exemplo, na
expressão a + b, temos o operador de aritmético + e operandos são as variáveis a e b.

Na linguagem Python temos a seguinte separação entre os diferentes tipos de operadores:

Operadores aritméticos
Operadores de atribuição
Operadores de comparação
Operadores lógicos
Operadores de identidade
Operadores de associação

------------------------------------------------------------------------------------------------------------------------

"+" = Adição, realiza a soma entre os operadores e concatenação de strings:
    print(10 + 3) => R: 7
    print('Olá ' + 'mundo!') => R: Olá mundo!

------------------------------------------------------------------------------------------------------------------------

"-" = Subtração, realiza a subtração entre operandos e adiciona o sinal negativo ao número:
    print(4 - 5) => R: -1

------------------------------------------------------------------------------------------------------------------------


"*" = Multiplicação, é representada pelo sinal de asterisco e realiza a multiplicação entre dois operandos ou repetição
    de strings:
    Ex:

    * Multiplicação com algarismos
    print(3 * 3) => R: 9

    * Repetição de strings
    print(3 * 'OI! ') => R: OI! OI! OI!

------------------------------------------------------------------------------------------------------------------------

"/" = Divisão, é representada por uma barra e realiza a divisão entre dois números, retornando um resultado de ponto
      flutuante (resto da divisão).
    print(5 / 2) => R: 2.5

------------------------------------------------------------------------------------------------------------------------

"//" = Divisão Inteira, é representado por duas barras. Realiza a divisão entre dois operandos e retorna um número
       inteiro, ignorando o resto da divisão.
     print(5 // 2) => R: 2

     NOTA: Se a divisão inteira for realizada com um dado 'float', o valor retornado continuará ignorando o resto da
     divisão, porém também será um dado float.

     Ex:
     print(9 // 3)   R: 3
     print(8 // 3)   R: 2    # Ignorou o resto
     print(8.3 // 3) R: 2.0  # Ignorou o resto e retornou um dado 'float'
     print(8.9 // 3) R: 2.0  # Ignorou o resto e retornou um dado 'float'
     print(8.1 // 3) R: 2.0  # Ignorou o resto e retornou um dado 'float'

------------------------------------------------------------------------------------------------------------------------

"%" = Módulo, apesar de ser representado pelo sinal de porcentagem, este operador realiza a divisão entre dois números
      e retorna apenas o resto desta divisão. 5 % 2 = "1"
    print(9 % 2) => R: 1

------------------------------------------------------------------------------------------------------------------------

"**" = Exponenciação, é representado por dois asteriscos, e faz o cálculo de um número elevado ao outro (potência).
     print(2 ** 3) => R: 8

------------------------------------------------------------------------------------------------------------------------
* Operadores e strings:
                       Podemos utilizar os operadores lógicos em conjunto com strings. Funcionarão para CONCATENAR tanto
                       quanto para REPETIR uma string. Para concatenar utilizamos o operador "+" e para repetir ou
                       multiplicar "*".
                       Ex:

                       # Repetição;
                       print(3 * 'oi ')
                       R: oi oi oi

                       # Concatenação;
                       print('olá ' + 'mundo!')
                       R: olá mundo!

                       NOTA: Não é possível utilizar a concatenação de um número (algarismo) com uma str. Esta operação
                       só será permitida entre duas strings.
                       Ex:
                       print(3 + '5') # R: error
------------------------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------------------------


"""


#======================================================================================================================
#======================================================================================================================

# OPERADORES

# Escreva um código que exiba os seguintes cálculos abaixo de acordo com esse modelo: Adição: 5 + 3 = "8"

# 33+8
# 10-17
# 9*4
# 8/3
# 8//3
# 8%3
# 8**3

print(f'Adição: 33 + 8 = "{33 + 8}"')
print(f'Subtração: 10 - 17 = "{10 -17}"')
print(f'Multiplicação: 9 x 4 = "{9 * 4}"')
print(f'Divisão: 8 / 3 = "{8 / 3}"')
print(f'Divisão inteira: 8 // 3 = "{8 // 3}" ')
print(f'Módulo da divisão: 8 % 3 = "{8 % 3}"')
print(f'Exponenciação: 8 ** 3 = "{8 ** 3}"')

# R: Adição: 33 + 8 = "41"
#    Subtração: 10 - 17 = "-7"
#    Multiplicação: 9 x 4 = "36"
#    Divisão: 8 / 3 = "2.6666666666666665"
#    Divisão inteira: 8 // 3 = "2"
#    Módulo da divisão: 8 % 3 = "2"
#    Exponenciação: 8 ** 3 = "512"

print('')
#======================================================================================================================

# OPERADORES COM STRINGS (concatenação e repetição)

# Utilizando os operadores lógicos "+" e "*", exiba as seguintes informações no console: Olá mundo!
#                                                                                        Olá! Olá! Olá!

print('Olá ' + 'mundo!')
print(3 * 'Olá! ')

# R: Olá mundo!
#    Olá! Olá! Olá!

print('')
#======================================================================================================================


print(9 // 3)
print(8 // 3)
print(8.3 // 3)
print(8.9 // 3)
print(8.1 // 3)


#======================================================================================================================





#======================================================================================================================




#======================================================================================================================




#======================================================================================================================




#======================================================================================================================





#======================================================================================================================
