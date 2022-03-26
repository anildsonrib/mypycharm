"""
ENTRADA DE DADOS - AULA 3
*A FUNÇÃO input('') SERVE PARA O CÓDIGO SOLICITAR ALGUMA INFORMAÇÃO DO USUÁRIO. UMA PERGUNTA SERÁ FEITA E O PROGRAMA
   FICARÁ AGUARDANDO UMA RESPOSTA.
*A FUNÇÃO input('') RECEBE UMA str E SEMPRE RETORNA UMA str COMO RESPOSTA.

"""

#nome = input('Qual é o seu nome? ')
#  VARIÁVEL CRIADA COM UMA FUNÇÃO input('') E UMA PERGUNTA QUE FOI ATRIBUÍDA À ESTA FUNÇÃO ('str').
#  SERÁ EXIBIDA UMA MENSAGEM NA TELA "Qual é o seu nome?" E O PROGRAMA FICARÁ AGUARDANDO UMA RESPOST.
#  QUALQUER COISA QUE FOR DIGITADA, IRÁ RETORNAR UM 'str' COMO RESPOSTA, MESMO QUE SEJA UM NÚMERO.

#print(f'O usuário digitou {nome} e o tipo da variável é '
#      f'{type(nome)}')
#  QUANDO O USUÁRIO FORNECER UMA RESPOSTA AO PROGRAMA, ESTA PARTE DO CÓDIGO SERÁ EXECUTADA. UMA NOVA MENSAGEM APARECERÁ
#        "O usuário digitou {o nome que foi fornecido anteriormente}" e o tipo da variável é {(tipo da variável)}

#nome = input('Qual o seu nome? ')
#idade = input('Qual a sua idade? ')
#ano_nascimento = 2022-int(idade)
# NESTE CASO, FOI NECESSÁRIO FAZER UM 'CASTING' NA VARIÁVEL 'idade', POIS NÃO DÁ PARA FAZER CALCULOS ENTRE NÚMEROS
#       INTEIROS 'int' E STRINGS 'str'. PARA RESOLVER O PROBLEMA, COLOCA-SE A 'str' 'idade' ENTRE PARENTESES E ADICIONA
#       UMA FUNÇÃO 'int' ANTES DELA. EX: idade ====> int(idade)
#print('') # O PRINT VAZIO SERVE PARA SALTAR UMA LINHA
#print(f'{nome} tem {idade} anos de idade. '
#      f'{nome} nasceu em {ano_nascimento}.')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite um outro número: ')
soma = numero_1+numero_2
print(f'A soma de {numero_1} + {numero_2} = {soma}')
# QUANDO ESSE CÓDIGO FOR EXECUTADO, ESPERA-SE QUE ELE SOME OS DOIS NÚMEROS QUE O USUARIO FORNECEU AO PROGRAMA, PORÉM O
#       CÓDIGO IRÁ CONCATENAR OS DOIS NÚMEROS. ISTO ACONTECE PELO FATO DE TODA A RESPOSTA RETORNADA PELA FUNÇÃO 'input'
#       SER UMA 'str'. EX: "3 + 4= 34"

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite um outro número: '))
soma = numero_1+numero_2
print(f'A soma de {numero_1} + {numero_2} = {soma}')
# NESTA PARTE DO CÓDIGO FOI REALIZADO UM CASTING NO INPUT DA VARIAVEL num_1 e num_2. AGORA SERÁ FEITA UMA SOMA DESSES
#      DOIS NÚMEROS.