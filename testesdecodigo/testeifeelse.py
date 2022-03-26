# Crie um código onde exiba uma pergunta sobre a idade do usuário.
# Ao fornecer os dados, o código irá classificar o usuário como 'criança', 'adolescente' ou 'adulto'.

'''
nome = input('Qual o seu nome, seu infeliz!!! ')
idade = int(input('...e qual é a sua idade, seu desajustado! '))
criança = 11
adulto = 18

if idade <= criança:
    print(f'{nome}, você é uma criança.')
elif idade < adulto and idade > criança:
    print(f'{nome}, você é um adolescente.')
else:
    print(f'{nome}, você é um adulto.')


nome = input('Qual o seu nome, seu infeliz!!! ')
idade = int(input('...e qual é a sua idade, seu desajustado! '))

if idade <= 12:
    print(f'{nome}, você é uma criança.')
elif idade < 18 and idade > 12:
    print(f'{nome}, você é um adolescente.')
else:
    print(f'{nome}, você é um adulto.')
'''

'''
nome = input('Qual o seu nome, seu infeliz!!! ')
idade = int(input('...e qual é a sua idade, seu desajustado! '))

if idade < 12:
    print(f'{nome}, você é uma criança.')
elif idade < 18:
    print(f'{nome}, você é um adolescente.')
else:
    print(f'{nome}, você é um adulto.')
    
    
nome = input('Qual o seu nome, seu infeliz!!! ')
idade = int(input('...e qual é a sua idade, seu desajustado! '))
criança = 11
adulto = 18

if idade <= criança:
    print(f'{nome}, você é uma criança.')
elif idade < adulto and idade > criança:
    print(f'{nome}, você é um adolescente.')
else:
    print(f'{nome}, você é um adulto.')
'''

nome = input('Qual o seu nome, seu infeliz!!! ')
idade = int(input('...e qual é a sua idade, seu desajustado! '))
criança = 11
adulto = 18

if idade < criança:
    print(f'{nome}, você é uma criança.')
elif idade < adulto:
    print(f'{nome}, você é um adolescente.')
else:
    print(f'{nome}, você é um adulto.')