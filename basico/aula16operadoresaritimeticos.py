"""
+  adição de dois números /concatenação de strings
-  subtração de dois números
*  multiplicação de dois números /multiplicação de strings
/  divisão com o resultado em um número 'float' (divisão quebrada)
// divisão inteira. O resultado dessa divisão retorna um número inteiro. Se o resultado for em um número quebrado, ele arredonda para mostrar um número inteiro.
** exponenciação ou potenciação. Seria um número elevado a outro.
%  resto da divisão. Retorna o módulo, ou seja, o resto da divisão entre um número e outro. Ex: 10/3=3 e resta 1
() utilizado para alterar a precedencia no cálculo, como em uma expressão numérica. Ex: 5+2*10='25'  /(5+2)*10='70'
"""

# Adição /Concatenação de 'str'
print('Soma 5+5=', 5 + 5) # Somou 10+10.
print('Soma /Concatenação 5+5=', '5' + '5') # Concatenou a str "Anildson" com a str "Ribeiro"

# Subtração
print('Subtração 10-5=', 10 - 5) # Fez a subtraiu 10-5

# Multiplicação /Multiplicação de 'str'
print('Multiplicação 10*10=', 10 * 10) # Fez a multiplicação de 10*10
print('Multiplicação "str" 10*10 str=', 10 * '10') # Repetiu a str '10' por 10x

# Divisão 'float'
print('Divisão "float" 10/5=', 10 / 5)

# Divisão Inteira
print('Divisão inteira 10//3=', 10 // 3)
print('Divisão inteira com "float" 10.0//3=', 10.0 // 3) #Retornou e um resultado de número flutuante, porém arredondado, pois o cálculo foi realizado com um número flutuante

# Exponenciação ou potenciação
print('Exponenciação de 2 elevado a 10=', 2 ** 10)

# Resto da divisão
print('Resto da divisão 10/3=3 e resta', 10 % 3) # Exibe o módulo, ou resto da divisão. Se dividir-mos 10/3, será igual a três e restará 1.
print('Resto da divisão 10/5=2 e resta', 10 % 5) # Como 10/5 não resta nada, o código retorna um valor '0'

# Alteração de precedência
print('Alteração da ordem do calculo 5+2*10=', 5 + 2 * 10) # Multiplica-se 2*10 e depois soma-se 5, resultando em 25
print('Alteração da ordem do calculo (5+2)*10=', (5 + 2) * 10) # O alterador de precedência '()' soma primeiro 5+2 e depois multiplica-se por 10, resultando em 70