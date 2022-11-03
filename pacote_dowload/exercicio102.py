"""Desafio 102
Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro indique o número a calcular e o outro
chamado show, que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial
"""


def fatorial(a, show=False):
    """
    -> Calcula o fatorial de um número.
    :param a: o número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: o valor do fatorial de um número
    """
    from math import factorial
    print('-' * 20)
    if show == True:
        print(f'{a}! = ', end='')
        for c in range(a, 0, -1):
            if c > 1:
                print(c, 'x ', end='')
            elif c == 1:
                print(f'{c} = ', end='')
        return f'{factorial(a)}'
    else:
        return f'{factorial(a)}'


# Programa Principal
print(fatorial(5, show=False))
