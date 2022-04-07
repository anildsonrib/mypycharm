"""
Faça um programa que peça o primeiro nome do usuário;
Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto.";
Se tiver entre 5 a 6 letras, escreva: "Seu nome é normal."
Maior que 6, escreva: "Seu nome é muito grande."
"""

nom = input('Digite o nome do usuário: ')
qtd = len(nom)

if qtd <= 4:
    print(f'{nom}, seu nome é curto.')
elif qtd <= 6:
    print(f'{nom}, eu nome é normal.')
else:
    print(f'{nom}, seu nome é muito grande')