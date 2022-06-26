"""


                                  AULA 15 - Tipos de dados "primitivos"

------------------------------------------------------------------------------------------------------------------------
* String:
          Na programação String representa um conjunto de caracteres disposto numa determinada ordem. A partir de agora,
          todas as vezes em que falarmos o termo String, estaremos nos referindo a um conjunto de caracteres.
          NOTA: Uma string vazia, quando for avaliada por um valor bool, irá sempre retornar um valor False.
          Ex: print(bool(''))
              R: False
------------------------------------------------------------------------------------------------------------------------
* Inteiro:
           Um segundo tipo de informação são os dados compostos por caracteres numéricos (algarismo). É considerado um
           número inteiro, qualquer algarismo positivo, negativo ou zero (...e que não possua ponto).
           NOTA_1: Atente-se para o fato de que, qualquer número inserido dentro de aspas passa a ser considerado uma str
           pelo interpretador. Ex: print(type('10'))
                                   R: <class 'str'>
           NOTA_2: O algarismo '0' retornará um valor 'False' se for checado por um valor booleano.
           Ex: print(bool(0))
               R: False
------------------------------------------------------------------------------------------------------------------------
Float (ponto flutuante):
                         No python não utilizamos virgula em algarismos. E dizemos que um número é 'float' ou de 'ponto
                         flutuante' quando ele tem casas decimais, ex: 8.6, 3.652, 0.0
                         NOTA_1: Atente-se para o fato de que, qualquer número inserido dentro de aspas passa a ser
                         considerado uma str pelo interpretador. Ex: print(type('0.7'))
                                                                     R: <class 'str'>
                         NOTA_2: O algarismo '0.0' retornará um valor 'False' se for checado por um valor booleano.
                         Ex: print(bool(0.0))
                             R: False
------------------------------------------------------------------------------------------------------------------------
* Bool:
        Em Python o tipo bool especifica os valores booleanos falso (False) e verdadeiro (True). Podemos criar variáveis
        associadas a booleanos, mas o uso mais comum é na verificação de resultados de expressões relacionais e lógicas.
        Ex: 10 == 10 => True
            20 < 15  => False
        NOTA: STRING VAZIA e DADOS FLOAT (0.0), quando checados por um valor bool retornarão um resultado False
        Ex: print(bool(''))  # string vazia   => R: False
            print(bool(0.0)) # dado float 0.0 => R: False
        NOTA_2: Números inteiros e float, diferentes de 0, retornarão o resultado True.
------------------------------------------------------------------------------------------------------------------------
* Type:
        A função 'type' exibe O TIPO de dado de um valor ou variável. O valor ou variável, que é chamado de
        argumento da função, tem que vir entre parênteses. É comum se dizer que uma função 'recebe' um valor ou mais
        valores e 'retorna' um resultado. O resultado é chamado "valor de retorno".
Ex:
print(type('verdura')) # Neste caso, o dado a ser classificado deve vir dentro de parênteses.
print(type(10))
print(type(3.5))
print(type(False))

R: <class 'str'>  # class (classificação do dado) ///'str' (tipo do dado)
   <class 'int'>
   <class 'float'>
   <class 'bool'>

------------------------------------------------------------------------------------------------------------------------
* Type Casting:
                É o método para converter o tipo de dados variável em um certo tipo de dados para que a operação seja
                executada pelos usuários.
                Ex: print(type(int(13.7)))
                    R: <class 'int'>   # O que deveria retornar um dado float, agora irá retornar um dado inteiro, pois
                                         foi realizado um casting.
                Podemos converter uma string (com dígitos) para um valor 'float' ou 'int', mas existem algumas regras:
                Ex: print("1", type(int('10')))
                    print("2", type(float('10')))
                    print("3", type(float('10.7')))
             #error print("4", type(int('3.7'))) # float não pode ser convertido para inteiro
             #error print("5", type(int('texto'))) # textos (com letras) não podem ser convertidos para inteiro
             #error print("6", type(float('texto'))) # textos (com letras) não podem ser convertidos para float

"""


#======================================================================================================================
#======================================================================================================================

# TYPE:

# Utilizando a função 'type', mostre no console a classificação dos seguintes dados à seguir:
# "verdura, 10, -12,5, False"

print(type('verdura'))
print(type(10))
print(type(-12.5))
print(type(20 >= 30))

# R: <class 'str'>
#    <class 'int'>
#    <class 'float'>
#    <class 'bool'>

print('')
#======================================================================================================================

# TYPE:

# Imprima no console o seu nome, sua idade, sua altura e se você é maior de 18 anos, classificando cada tipo de dado
# utilizando a função 'type'.

# nome
print('Anildson', type('Anildson'))

# idade
print('37', type(37))

# altura
print(1.75, type(1.75))

# é maior de idade?
print(37 > 18, type(37 > 18))

# R: Anildson <class 'str'>
#    37 <class 'int'>
#    1.75 <class 'float'>
#    True <class 'bool'>
#======================================================================================================================

