"""DESAFIO 060
Faça um programa que leia um número qualquer e mostre o seu fatorial
Exemplo: 5! = 5x4x3x2x1=120
com o for e while"""
num = int(input('Digite um valor: '))
print(f'{num}!=', num, 'x', end=' ')
cont = num
acumuladora = 0
for c in range(num - 1, 0, -1):
    if cont == num:
        acumuladora = num * c
        cont -= 1
    else:
        acumuladora = acumuladora * c
        cont -= 1
    if c != 1:
        print(c, end=' x ')
    else:
        print(c, end='')

print(f' =', acumuladora)
