#  *Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa.
#  *Criar variável para o ano atual (int)
#  *Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
#  *Obter o imc da pessoa com duas casas decimais (peso e na altura da pessoa)
#  *Exibir um texto com todos os valores na tela usando f'strings (com as chaves)

nome = 'Anildson'
idade = 37
altura = 1.75
peso = 90.0
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(15*'=')
print(f'{nome} tem {idade} anos, {altura}m de altura e pesa {peso}Kg.')
print(f'O IMC de {nome} é de {imc:.2f}')
print(f'Anildson nasceu em {nascimento}')
print(15*'=')


