"""DESFIO 061
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão aritmética usando
a estrutura while."""

"""Desafio 051
Desenvolva um programa que leia o primeiro termo e a razão de um PA - progressão aritmética .
No final, mostre os 10 primeiros termos dessa progressão.
... é uma contagem que vai pulando de tanto até tanto - de 1 até 100, pulando de 10 em 10, isso é uma PA
onde o primeiro elemento é 1 e o último é 10 (razão)"""

print('Gerador de PA')
print('==-==' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('Fim')