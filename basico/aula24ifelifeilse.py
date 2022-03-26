"""
AULA 24 - CONDIÇÕES IF ELIF E ELSE

"""
"""
if True:
    print('Verdadeiro.') #  ESSA LINHA SÓ SERÁ EXECUTADA SE A LINHA ANTERIOR FOR VERDADEIRA.

    num_1 = 2
    num_2 = 2

    print(num_1 + num_2) #  O BLOCO DE CÓDIGO QUE SEGUIU, SERÁ TAMBÉM EXECUTADO POIS ESTÁ NA MESMA HIERARQUIA DE 'if True'
"""

"""
if False:
    print('Verdadeiro.') #  NESSE CASO, ESSE BLOCO NÃO FOI EXECUTADO POIS A CONDIÇÃO ANTERIOR FOI CHECADA COMO FALSA.
                         #  ENTÃO O LEITOR SALTOU PARA A PRÓXIMA LINHA.
print('A minha expressão não é verdadeira.')
"""

if False:
    print('Verdadeiro.')
elif True:
    print('Agora é verdadeiro.')
    nome = input('Digite seu nome. ')

    print(f'Seu nome é {nome}.')
else:
    print('Essa expressão não é verdadeira')