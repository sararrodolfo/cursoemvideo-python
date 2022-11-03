"""DESAFIO 060
Faça um programa que leia um número qualquer e mostre o seu fatorial
Exemplo: 5! = 5x4x3x2x1=120
com o for e while"""

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
