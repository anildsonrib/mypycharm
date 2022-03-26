"""
usuario = input('Digite seu usuário: ')
qtd_car = len(usuario)

print(usuario, qtd_car, type(qtd_car))

senha = input('cadastre uma senha: ')
qtd = len(senha)

if qtd < 6:
    print('Digite no mímino 6 caracteres.')
else:
    print('usuário cadastrado.')

string_1 = input('digite: ')
string_2 = input('digite outra coisa: ')

print(f'A quantidade total de caractere é de {len(string_1) + len(string_2)}')
"""
print(len('anildson'))
print(len(True))
