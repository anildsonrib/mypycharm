"""
TIPOS DE DADOS
str - string     textos, ou coisas que estão dentro de aspas simples 'assim' ou duplas "assim"
int - inteiro      é um numero positivo, negativo ou 0 e que NÃO tenha ponto, 123456 -1  -5  0  35  68
float -    real/ponto flutuante. Também é um número negativo, negativo ou 0 e que tenha ponto -1.3  -5.2  0.0  35.2  68.7
bool - booleano/lógico   possui apenas dois valores, pois ele checa a lógica do código, retornando um resultado TRUE ou FALSE (verdadeiro ou falso)
ex: 10==10? TRUE
    10==11? FALSE
"""


print('Luiz', type('Luiz'))
# *Função 'type' serve para identificar qual é o tipo de dado utilizado.
# *Neste caso foi uma 'str'. Resultado= Luiz <class 'str'>

print('10', type('10'))
# *Quando qualquer número estiver dentro de aspas, ele será considerado uma 'str'
# *Resultado= 10 <class 'str'>

print(10, type(10))
# *Neste caso o '10' está fora das aspas e será considerado pelo código como um número inteiro (positivo ou negativo/sem pontos)
# *Resultado= 10 <class 'int'>

print(25.23, type(25.23))
# *Resultado= 25.23 <class 'float'>

print(10 == 10, type(10 == 10))
# *O duplo sinal de igual "==", NÃO ESTÁ AFIRMANDO que um número é igual ao outro, ele está PERGUNTANDO se um número é igual ao outro.
# *Neste caso, ele pergunta se 10 é igual a 10, e retorna um resultado 'TRUE', pois 10 é realmente igual a 10.
# *Resultado= True <class 'bool'>

print('L' == 'l', type('L' == 'l'))
# *Aqui, ele pergunta se 'L' maiúsculo é igual a 'l' minúsculo. E retorna um valor 'FALSE', pois os mesmos não são iguais.
# *Resultado= False <class 'bool'>