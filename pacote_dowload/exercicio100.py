"""Desafio 100
Faça um programa que tenha uma lista chamada números
e duas funções chamada sorteio() e somaPar()
A primeira função vai sortear 5 números e vai colocá-los
dentro de uma lista e a segunda função vai mostrar a soma
entre todos os valores sorteados pela função anterior, ou seja,
a do sorteio.
"""
from random import randint
from time import sleep


def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'A soma dos valores pares de {lista}, temos {soma}.')

# Programa principal
numeros = list()
sorteio(numeros)
somaPar(numeros)