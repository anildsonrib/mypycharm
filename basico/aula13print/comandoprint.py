"""

                                  Aula 13 - O comando (função) print

------------------------------------------------------------------------------------------------------------------------

* A função print() em Python:
                              A função print() é uma das funções mais importantes e usadas na linguagem Python. Sua
                              função é, basicamente, exibir mensagens na tela ou enviá-las para outro dispositivo, como
                              imprimir dentro de arquivos de texto.

* A informação contida dentro do comando 'print' é chamada de argumento. Argumentos são tipos de dados.

Ex:
    print(123456) # Tudo que for colocado entre parenteses será exibido na tela.
    R: 123456

------------------------------------------------------------------------------------------------------------------------

* sep='separador':
                É um parâmetro de função que especifica como os objetos serão separados, se houver mais do que um. O
                padrão é um espaço em branco.
Ex:
    print('Anildson', 'Sousa', 'Ribeiro', sep='*') # O parametro (argumento nomeado) 'sep' definiu que os argumentos
                                                     dentro da função print seriam separados por um asterisco.

R: Anildson*Sousa*Ribeiro.

* Quando o parâmetro 'sep' recebe alguma informação dentro de suas aspas, ele passa a ser um argumento nomeado.

------------------------------------------------------------------------------------------------------------------------

* Argumento nomeado:
                      Argumento nomeado é um recurso que permite a passagem de valores pela associação chave-valor e
                      assim, os mesmos não precisaram estar dispostos numa ordem pre-estabelecida, até porque, o Python
                      receberá um dicionário que contém o nome e o valor de cada parâmetro.
Ex: O parâmetro de função sep='' quando recebe alguma valor dentro de suas aspas (sep='*') e está contido em uma função
print, ele passa a ser um ARGUMENTO NOMEADO.

------------------------------------------------------------------------------------------------------------------------
* end='':
          O parâmetro end= da função print:
          Por padrão, a função print utiliza a quebra de linha (\n) como último caracter. O parâmetro end= é responsável
          por alterar esse comportamento, possibilitando ao desenvolvedor trocar qual caracter será  adicionado ao final
          do dado impresso no terminal.

          Vamos entender melhor no exemplo a seguir:

# Exemplo com fim de linha sem nenhum caracter
print('Vamos estudar Na ', end='')
print('Python Academy')

R: Vamos estudar Na Python Academy
Como o parâmetro end não recebeu nenhum valor, automaticamente ele desativou a quebra de linha escondida que havia no
final do código. Então o argumento do segundo print foi mostrado na mesma linha que o primeiro.


# Exemplo com fim de linha igual à ->
print('As rosas são', end=' -> ')
print('Vermelhas')

R: As rosas são -> Vermelhas
Agora, diferente do primeiro exemplo, transformamos o parâmetro em um argumento nomeado. Ele mostrou no console os
argumentos do primeiro print na mesma linha que o segundo, separando-os por pela string '->'.


# Exemplo com fim de linha igual à :
print("Quantidade", end=': ')
print(40)

R: Quantidade: 40
Um segundo exemplo do parâmetro end como argumento nomeado.



"""

#======================================================================================================================
#======================================================================================================================

# PRINT
# Com a função 'print', exiba uma sequencia de numeros no console de 1 a 6

print(123456)
print('')

# R: 123456

#======================================================================================================================

# PRINT
# Mostre no console o seu nome completo, como no exmplplo: "Anildson de Sousa Ribeiro"

print('Anildson', 'de', 'Sousa', 'Ribeiro')
print('')

# R: Anildson de Sousa Ribeiro

#======================================================================================================================

# SEP

# Utilizando o parametro de função 'sep' como argumento nomeado, escreva um código que separe seu nome e sobrenome por
# virgulas, asteriscos e barras.

print('Anildson', 'Sousa', 'Ribeiro', sep=',')
print('Anildson', 'Sousa', 'Ribeiro', sep='*')
print('Anildson', 'Sousa', 'Ribeiro', sep='/')
print('')

# R: Anildson,Sousa,Ribeiro
#    Anildson*Sousa*Ribeiro
#    Anildson/Sousa/Ribeiro

#======================================================================================================================

# END

# "Te esperei o dia inteiro "
# "e você não apareceu."

# 1 - Mostre no console as frases em linhas separadas (dois prints);
# 2 - Mostre no console as frases em linhas separadas (utilizando a quebra de linha);
# 3 - Mostre as frases na mesma linha (utilizando dois prints);
# 4 - Mostre as frases separadas por vírgula;
# 5 - Mostre as frases separadas por barras duplas;

print('1 - Te esperei o dia inteiro ')
print('e você não apareceu.')
print('')
print('2 - Te esperei o dia inteiro', '\ne você não apareceu.')
print('')
print('3 - Te esperei o dia inteiro', end=' ')
print('e você não apareceu.')
print('')
print('4 - Te esperei o dia inteiro', end=', ')
print('e você não apareceu.')
print('')
print('5 - Te esperei o dia inteiro ', end='// ')
print('e você não apareceu.')