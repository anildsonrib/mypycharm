num1 = float(input("Digite 1º número: "))
num2 = float(input("Digite 2º número: "))
num3 = float(input("Digite 3º número: "))


def ler_numeros():
    print(f'Os números lidos são: {num1}, {num2} e {num3}')


def soma():
    soma = (num1 + num2 + num3)
    print(f'O resultado da soma é: {soma}')


def media():
    media = (num1 + num2 + num3) / 3
    print(f'A média é: {media}')


ler_numeros()
soma()
media()