"""
a = 2
b = 2
c = 3

if a == b and b < c:
    print('True')
else:
    print('False')


if a == b and b > c:
    print('True')
else:
    print('False')

if a == b or b < c:
    print('True')
else:
    print('False')

if a != b or b > c:
    print('True')
else:
    print('False')


a = 3
b = 2

if b > a:
    print('B é maior do que A')
else:
    print('A é maior que B')


a = ''
b = 0

if not a:
    print('Preencha "A"')


nome = 'caipira'

if 'u' in nome:
    print('Existe "u"')
else:
    print('Não existe "u"')


nome = 'bicicleta'

if 'pai' not in nome:
    print('Não existe')
else:
    print('Existe')
"""

usu = input('Usuário: ')
sen = input('Senha: ')
usu_bc = 'anildson'
sen_bc = '853021'

if usu == usu_bc and sen == sen_bc:
    print('Login realizado com sucesso: ')
else:
    print('Usuário ou senha inválidos.')