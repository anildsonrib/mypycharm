"""
FOR IN - ESTRUTURAS DE REPETIÇÃO
* O laço 'while' é utilizado para iterar em strings onde não sabemos o seu fim.
 O laço 'for' serve para iterar-mos em estrutras finitas, onde sabemos o seu fim.
* Exemplo utilização do laço for:

  texto = 'Python'

  for letra in texto: # para cada item (letra) na var 'texto'...
  print(letra)        # ...imprima este item. O laço 'for' vai ficar iterando em cada índice da string 'Python' e imprimindo
                      # até que não haja mais índices a serem impressos.

* A função range(), quando utilizada no código, irá retonar um conjunto de números sequencias pre setadas pelo usuário
Ex: range(10), o resultado no console será, 1 2 3 4 5 6 7 8 9
    range(2, 5) o resultado será 2 3 4 (lembrando que se eu escolho de até 5, ele só mostra até o 4)
* A função range recebe três argumentos: range(start0, stop, step1). O primeiro vai definir de onde começará a contagem.
O segundo definirá onde irá parar e o últmimo diz de quanto em quanto será o incremento.
ex: range(3, 10, 2) o resultado será 3 5 7 9

*break = termina o laço /continue = pula para o próximo laço.

"""

# texto = 'Python'
# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

# texto = 'Python'
#
# for letter in texto:
#     print(letter)
#
#
# texto = 'Python'
#
# for n, letter in enumerate(texto):
#     print(n, letter)

# for i in range(3, 10, 2): # começa em 3, para em 10 e incrementa de 2 em 2.
#     print(i)
#
# print('')
#
# for i in range(20, 10, -1):  #  com o star é maior que o stop, o incremento (step) tem de ser negativo (decremento) para
                               #  ele contar de trás para frente. Como foi solicitado que parasse no 10, ele mostrou somente
    # print(i)                 #  até o 11.

#***************************************************************

# Crie um código que mostre os números múltiplos de 8 até 100:

# for n in range(0, 101, 8):
#     print(n)
#
#Crie um código que mostre os números múltiplos de 8 até 100, utilizando 'if':
#
# for n in range(100):
#     if n % 8 == 0:
#         print(n)
#
# Crie um código utilizando 'for' que mude a letra do 't' do texto 'Python' para maiúscula.

# texto = 'Python'
# new_tr = ''
#
# for n in texto:     # para cada item (que foi definido como 'n' na var texto...
#     if n == 't':    # cheque se existe um 't' minúsculo...
#         new_tr += n.upper()   #...se houver, tranforme esse 't' em maiúsculo com a função .upper() e concatene com os itens da var new_str.
#     elif n == 'h':      # cheque se existe um 'h' minúsculo...
#         new_tr += n.upper() #...transforme esse 'h' em maiúsculo com a função .upper() e concatene com os itens da var new_str.
#     else:
#         new_tr += n     # quando não houver nem 't' e nem 'h', simplesmente concatene os itens de 'n' e atribua-os à var 'nov_str'.
# print(new_tr)       #quando terminar de iterar sobre a str 'texto', imprima os dados da var 'nov_str' que terá agora o 'T' e o 'H' maiúsculo.

#**************************************************************************

#Crie um código que não imprima a letra 'o' no texto: "O rato roeu a roupa do rei de roma"

# texto = '"O rato roeu a roupa do rei de roma"'
# new_str = ''
#
# for n in texto:
#     if n == 'o' or n == 'O':
#         continue
#     else:
#         new_str += n
# print(new_str)

#**************************************************************************

# Crie um código que pare de executar quando ele encontrar a letra 'd' no texto 'anildson'

texto = 'anildson'
n_t = ''

for n in texto:
    if n == 'd':
        break
    else:
        n_t += n

print(n_t)