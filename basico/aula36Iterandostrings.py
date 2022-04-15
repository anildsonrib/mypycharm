"""
* 'Iterar' quer dizer que o código irá percorrer cada elemento da string;
* Para iterar um elemento, ele precisa ser 'iterável', ou seja, ele precisa ter índices (0, 1, 2, 3, 4, ...).
*
"""

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_str = ''
input_do_usuario = input('Qual letra deseja colocar maiúscula?: ')
tamanho_input = len(input_do_usuario)

if input_do_usuario not in frase:
    print('Você não digitou uma letra contida na frase. Digite uma letra válida.')
elif tamanho_input > 1:
    print('Digite apenas uma letra')
else:
    while contador < tamanho_frase:
        letra = frase[contador]
        if letra == input_do_usuario:
            nova_str += input_do_usuario.upper()
        else:
            nova_str += letra
        contador += 1

    print(nova_str)

