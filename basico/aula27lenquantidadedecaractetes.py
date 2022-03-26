"""
A FUNÇÃO 'len'
  A função len serve para contar a quantidade de caracteres que tem dento de uma str.
  Um exemplo de aplicação seria em um login, onde o sistema precisa checar a quantidade mínima de caracteres digitados
  pelo usuário (uma senha) para fazer o cadastro.
  Vale ressaltar e essa função não funciona com estilos numéricos (float, int,)
  A função 'len' sempre retorna um resultado do tipo 'int', ou seja, com o resultado pode-se fazer calculos.



#  Ex 1: Fazendo a contagem de caracteres e classificando o resultado.
usuario = input('Digite o nome de usuário: ')
qtd_carac = len(usuario)

print(usuario, qtd_carac, type(qtd_carac))


#  Ex 2: Código vai fazer a contagem e julgar se foi uma quantidade mínima digitada.

usuario = input('Digite o nome de usuário: ')
qtd_carac = len(usuario)

if qtd_carac < 6:
    print('Você precisa digitar pelo menos 6 caracteres: ')
else:
    print('Usuário cadastrado com sucesso.')


#  Ex 3: Somando a quantidade total de duas strings

nome = input('Digite o seu nome: ')
sob = input('Digite o seu sobrenome: ')

print(f'A quantidade total de caracteres foi de {len(nome) + len(sob)} palavras.')

"""

#  Ex 4: Um outro jeito de somar a quantidade total de strings.

nome = input('Digite o seu nome: ')
sob = input('Digite o seu sobrenome: ')
qtd_carac = len(nome) + len(sob)

print(f'A quantidade total de caracteres digitados foi de {qtd_carac} palavras.')