'''

Aula 29 - Pass e Ellipses como Placeholders

 'pass' => Pass
 '...'  => Elipses
 São recursos utilizados no python para guardar um espaço no código para ser escrito porteriormente.
 Isso evita um erro na execução do código quando , quando este for solicitado.



#  Exemplo 1:

valor = True

#  Como valor é True, a linha 'if' foi executada.
if valor:
    print('Se esse print apareceu, NÃO foi utilizado o PlaceHolder.')
else:
    print('Se esse print apareceu, "valor" é "false"')


#  Exemplo 2:

valor = False

#  Como 'valor' é False, a linha 'else' foi executada.
if valor:
    print('Se esse print apareceu, NÃO foi utilizado o PLaceHolder')
else:
    print('Se esse print apareceu "valor" é "false"')
'''

#  Exemplo 3:

valor = True

#  Neste caso, foi utilizada a PlaceHolder 'pass', para deixar a linha em branco (por enquanto) e não provocar um erro
#  na execução do código. Mesmo que 'if' verifique o valor como 'True' ele não executará nem a linha 'if' e nem a 'else'
if valor:
    pass
else:
    print('Se esse print apareceu "valor" é "false"')