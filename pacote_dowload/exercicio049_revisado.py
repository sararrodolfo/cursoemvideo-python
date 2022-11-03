"""Desafio 049
Refaça o DESAFIO 009 mostrando a tabuada de um número,
só que agora utilizando um laço for"""
"""Desafio 009 - TABUADA
leia um número inteiro
mostre a sua tabuada"""
numero = int(input('Qual tabuada gostaria de ver? '))
for c in range(0, 11):
    print(f'{numero} x {c} = {numero * c}')
print('Programa tabuada encerrado.Volte sempre.')