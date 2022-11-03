"""Desafio 098
Faça um programa que tenha uma função chamada contador()
que receba três parâmetros: início, fim, passo e realiza a contagem
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10 de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep


def contador(i, f, p):
    """
    -> Contador personalizado
    :param i: início da contagem
    :param f: final da contagem
    :param p: passos
    :return: sem retorno
    Função criada por Sara Regina para Treinamento de Funções
    """
    if p == 0 or p == []:
        p = 1
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {-p if p < 0 else p} em {-p if p < 0 else p}')
    if i < f:
        for n in range(i, f + 1, p):
            sleep(0.1)
            print(f'{n} ', end='')
        print('FIM!')
    elif f < i:
        if p > 0:
            p = - p
        for n in range(i, f - 1, p):
            sleep(0.1)
            print(f'{n} ', end='')
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)
