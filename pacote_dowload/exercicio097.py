"""Desafio 097
Faça um programa que tenha a função escreva()
que recebe um texto qualquer como parâmetro e mostre
uma mensagem com tamanho adaptável
Ex: escreva("Olá Mundo")
Saída:
----
Olá, Mundo!
----
A linha segue a quantidade de letras
"""


def escreva(msg):
    print('~' * 2 * len(msg))
    print(f'{msg:^}')
    print('~' * 2 * len(msg))


# Programa Principal
mensagem = str(input('Digite a mensagem: '))
escreva(mensagem)
