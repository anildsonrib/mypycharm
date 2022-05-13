"""
Aula 40 - For /Else em python

* Uma lista, nada mais é que uma variável onde podemos adicionar vários dados e acessá-los posteriormente. Uma lista é
    criada com vários dados entre colchetes [].

* A função startswith() é usada para verificar se uma determinada frase começa com alguma string particular.
   Os parâmetros de início e término são opcionais.
   Podemos usá-los quando quisermos que apenas alguma substring particular da string original seja considerada para
   pesquisa.
   Retorna: o valor de retorno é binário. A função retorna True se a frase original começar com search_string, senão
   False .

   termina com()

   Sintaxe:
   str.endswith (search_string, start, end)

   Parâmetros:
   search_string: a string a ser pesquisada.
   start: inicia o índice do str de onde search_string deve ser pesquisada.
   end: Índice final do str , que deve ser considerado para pesquisa.


"""

#======================================================================================================================

# Crie um código que leia uma lista com vários nomes próprios, e itere sobre essa lista e diga se algum dos nomes começam
# com a letra 'j'. Caso nenhum nome comece com a tal letra, imprima uma mensagem dizendo que nenhuma dos nomes começam
# com essa letra.

nomes = ['Anildson', 'Lucas', 'joão', 'Pedro', 'thiago', 'Hermanoteu']

# for item in nomes:
#     if item.lower().startswith('j'):
#         print(f'Começa com a letra J: {item}')
#     else:
#         print(f'Não começa com a letra J: {item}')

#======================================================================================================================

# Crie um código que verifique se existe algum nome que comece com a letra J dentro de uma lista e retorne uma mensagem
# dizendo se existe ou não existe.

# nomes = ['Anildson', 'Lucas', 'joão', 'Pedro', 'thiago', 'Hermanoteu']
# comeca_com_j = False
#
# for valor in nomes:
#     if valor.lower().startswith('j'):
#         comeca_com_j = True
#
# if comeca_com_j == True:
#     print('Existe uma palavra que começa com "J"')
# else:
#     print('Não existe uma palavra que comeca com "J"')

#======================================================================================================================
