"""Desafio 074

Crie um programa que gere cinco números aleatórios e colocar numa tupla
depois disso, mostre a listagem de números
também indique o menor e o maior valor que estão na tupla
Os valores sorteados foram: ----
O maior valor sorteado foi x
O menor valor sorteado foi y

"""
from random import randint
n1 = randint(0, 10)
n2 = randint(2, 10)
n3 = randint(0, 10)
n4 = randint(5, 10)
n5 = randint(0, 10)
sorteados = ''
print(f'Os valores sorteados foram: {sorteados}')
cont = maior = menor = 0
while cont <= 4:
    if cont == 0:
        maior = sorteados[cont]
        menor = sorteados[cont]
    else:
        if sorteados[cont] > maior:
            maior = sorteados[cont]
        if sorteados[cont] < menor:
            menor = sorteados[cont]
    cont += 1
print(f'O maior número sorteado foi: {maior}')
print(f'O menor número sorteado foi: {menor}')
