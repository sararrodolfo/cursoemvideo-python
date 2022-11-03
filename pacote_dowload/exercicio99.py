"""Desafio 099
Faça um programa que tenha uma função chamada maior()
que receba vários parâmetros com valores inteiros
seu programa tem que analisar todos os valores
e dizer qual deles é maior
Analisando os valores passados...
Foram informados {} valores ao t.o.d.o
O maior valor informado foi {}
Foram informados 0 valores ao ....
O maior valor foi zero
"""


def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    print(num, end=' ')
    tam = len(num)
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor foi {max(num)}.')
    print('-=' * 30)


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7,0)
maior(1, 2)