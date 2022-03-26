"""
AULA 26 - OPERADORES LÓGICOS
and
or
not
in
not in

#  (verdadeiro e verdadeiro) = retorna um valor 'true' /as duas expressões precisam ser verdadeiras para que se retorne um valor verdadeiro.
#  (verdadeiro e falso) = retorna um valor 'false'
comp1 and comp2

#  (verdadeiro ou verdadeiro) = retorna um valor 'true' /uma das comparações precisam ser verdadeiras para retornar um valor 'true'. Somente retorna um valor falso se as duas forem falsas.
comp1 or comp2

#  exemplos:

a = 2
b = 3

if b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')


a = 2
b = 3

if not b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')


nome = 'Anildson'
if 'Anil' not in nome:
    print('Executei')
else:
    print('Existe o texto')
"""

usuario = input('Nome do usuário: ')
senha = input('Senha: ')

usuario_bd = 'anildson'
senha_bd = '5733'

if usuario == usuario_bd and senha == senha_bd:
    print('Você está logado no sistema.')
else:
    print('**Usuário ou senha inválidos**')