"""Desafio 096
Faça um programa que tenha a função area(), que receba
as dimensões de um terreno retangular(largura e comprimento) e
mostre a área do terreno
"""

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg}x {comp} é de {a:.1f}m2.')


# Programa Principal
print('Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
