"""


                                  AULA 14 - Strings (texto) e aspas em Python

------------------------------------------------------------------------------------------------------------------------
* O que é string em Python?
                             * Strings, não somente em Python, mas também em outras linguagens de programação, são
                             conjuntos de caracteres de texto que podem ser compreendidos como representações de
                             informações escritas dentro de um código.
                             * String é um tipo de dado primitivo.
                             * Uma string é classificada como 'str' em python.
                             * Basicamente, strings são textos dentro de aspas simples ou duplas.
                             * Como o python é uma linguagem de tipagem dinâmica, toda vez que o interpretador encontrar
                             algum dado dentro de aspas, ele o identificará como uma string.

Exemplo da utilização das aspas em str:

print('Este texto contém uma "string" dentro dele')

R: Este texto contém uma "string" dentro dele
Nota: Como o código foi aberto com uma aspa simples, ele irá procurar a próxima aspa simples para fechar o comando, ou
seja, repare que existe dentro da linha de código outro dado dentro de aspas duplas. O interpretador irá considerá-lo
como parte da string e exibirá "string" como parte do texto.
------------------------------------------------------------------------------------------------------------------------
* Caractere de escape:
                        * Para inserir caracteres ilegais em uma string, use um caractere de escape. Um caractere de
                        escape é uma barra invertida \seguida pelo caractere que você deseja inserir.
                        * Um exemplo de caractere ilegal é uma aspa dupla dentro de uma string que é cercada por aspas
                        duplas:
                        * Esse método não é muito utilizado pois pode deixar o código um pouco confuso de se entender.
                        Outro detalhe é que a barra invertida também é utilizada em outros parâmetros, como por exemplo
                        a quebra de linha \n
Exemplo
Você receberá um erro se usar aspas duplas dentro de uma string cercada por aspas duplas:

print("We are the so-called "Vikings" from the north.")
Para corrigir esse problema, use o caractere de escape \":

Exemplo
O caractere de escape permite que você use aspas duplas quando normalmente não seria permitido:

print("We are the so-called \"Vikings\" from the north.")

R: We are the so-called "Vikings" from the north.
NOTA: As barras inseridas antes de cada aspa dupla dentro da palavra Vikings, fez com que o interpretador ignorasse o
erro e imprimisse a palavra como parte do texto. Lembrando que o código foi aberto também com aspas duplas.


"""
#======================================================================================================================
#======================================================================================================================


# CARACTERE DE ESCAPE

# Utilizando o caractere de escape, imprima o seguinte texto: Tudo no mundo real "vai" volta. Inicie o código também
# com aspas duplas para poder usar o caractere de escape.

print("Tudo no mundo real \"vai\" volta.")

# R: Tudo no mundo real "vai" volta.

#======================================================================================================================
