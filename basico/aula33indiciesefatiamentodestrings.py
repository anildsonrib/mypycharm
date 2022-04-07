"""
AULA 33 - ÍNDICES E FATIAMENTO DE STRINGS EM PYTHON

*STRINGS INDICES
*FATIAMENTO DE STRINGS [INICIO:FIM:PASSO]
*FUNÇÕES BUILT IN, LEN, ABS, TYPE. PRINT. ETC...

ESSAS FUNÇÕES PODEM SER USADAS DIRETAMENTE EM CADA TIPO.

"""

#  cada caracter desta string tem um índice, sendo que o primeiro caractere começa em 0. Ou seja P=0, y=1, t=2, h=3, o=4,
#  n=5, 'espaço'=6, s=7, 2=8.
#  positivos
texto = 'Python s2'

#  Para acessar um índice dentro da variável 'texto' utilizando a função print. eu tenho que colocar a var texto dentro
#  dos parenteses, abrir colchete, indicar a posição que eu quero acessar e fechar colchete.
#  Ex: para acessar a letra 't', eu vou indicar a posição 2.
# print(texto[2])  #  R: t

#  Para acessar, no caso, o último caracter (2), eu devo indicar o índice 8.
# print(texto[8])   #  R: 8

#  Perceba que a o ídice '6' é um espaço, e toda vez que ele for chamado no código, não exibirá nada na tela.
# print(texto[6])  #  R: ' '

#  Se eu tentar acessar o ídice '9' haverá uma mensagem de erro, pois esta cadeia possui apenas 8 carateres.
# print(texto[9])  #  R: ERRO! string index out of range

#  Existem ainda os índices negativos. São contados de trás para frente com números negativos. Serve para achar o último
#  item em uma string. Ex 'P   y   t   h   o   n      s   2'
#                       [ -9  -8  -7  -6  -5  -4  -3 -2  -1]

#  O fatiamento serve para acessar apenas uma parte de uma string. Por exemplo, na string 'Python s2', se quisermos
#  acessar apenas a parte 'thon' dessa string...
#  Chamei a função print para mostrar a var 'texto' do índice 2 ao ídice 6, mas ele não mostrará o índice 6 (que é um...
#  ...espaço, mostrará até o 5) R: thon
print(texto[2:6])

#  Quando eu quiser que o interpretador acesso a string desde o início até um certo ponto, eu não preciso indicar o
#  início, apenas onde eu quero que ele pare, pois ele subentende que o primeiro seja o zero. Coloco apenas os dois
#  pontos e a posição que eu quero que ele pare.
print(texto[:6])  #  R: Python

#  Caso eu queira imprimir somente o 's2', eu preciso indicar somente onde vai começar, mas não preciso indicar o fim,
#  pois o interpretador lerá até o fim da srting.
print(texto[7:])

#  Quando eu não sei qual é a quantidade de itens em uma string, e queira acessar, por exemplo, o penúltimo item ('s').
#  Eu vou usar o índice negativo.
print(texto[-2])  #  R: s

#  Se eu quiser acesar até o penultimo índice de uma cadeia de caractere, mas não sei quantos caracteres exatamente tem,
#  eu posso colocar os dois pontos (o interpretador entenderá que vai começar do 0...) e indicar até o -1, então ele
#  mostrará até o -2.
print(texto[:-1])  #  R: Python s

#  Uma das formas de fatiamento é o 'step' (passo). Posso mandar o interpretador ler uma cadeia de caractere porém ir
#  saltando alguns. Exemplo, print(texto[0:6:2]). Ele vai mostrar do caracter 0 ao 5 pulando de dois em dois.
print(texto[0:6:2])  #  R: Pto  (0, 2, 4)

#  Neste exemplo, vamos acessar do primeiro caracter até o final, saltando de 3 em 3. print(texto[0::3]). Observe que,
#  como vamos até o final, não precisaremos de indicar o índice após os dois pontos, ele ficará vazio e só indicaremos
#  depois o step.
texto_2 = 'Python_s2'
print(texto_2[0::3])  #  R: Ph_

#  Exemplo da função 'len'
print(len(texto_2))  #  R: 9