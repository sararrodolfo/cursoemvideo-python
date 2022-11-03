"""DESAFIO 060
Faça um programa que leia um número qualquer e mostre o seu fatorial
Exemplo: 5! = 5x4x3x2x1=120
com o for e while"""

num = int(input('Digite um valor: '))
contador = num
acumuladora = 0
print(num, '! = ', num, 'x', end=' ')
while contador > 1:
    if contador == num:
        acumuladora = num * (contador - 1)
        contador -= 1
    else:
        acumuladora = acumuladora * (contador - 1)
        contador -= 1
    if contador > 1:
        print(contador, 'x', end=' ')
    else:
        print(contador, end='')
print(' =', acumuladora)
