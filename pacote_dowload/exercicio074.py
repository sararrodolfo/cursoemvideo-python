"""Desafio 074

Crie um programa que gere cinco números aleatórios e colocar numa tupla
depois disso, mostre a listagem de números
também indique o menor e o maior valor que estão na tupla
Os valores sorteados foram: ----
O maior valor sorteado foi x
O menor valor sorteado foi y

"""
from random import randint
cont = menor = maior = 0
print(f'Os valores sorteados foram:', end=' ')
while cont <= 4:
    computador = randint(1, 10)
    print(computador, end=' ')
    n_aleatorio = computador
    if cont == 0:
        maior = n_aleatorio
        menor = n_aleatorio
    else:
        if n_aleatorio > maior:
            maior = n_aleatorio
        if n_aleatorio < menor:
            menor = n_aleatorio
    cont += 1
# print('')
print(f'\nO maior valor sorteado foi: {maior} ')
print(f'O menor valor sorteado foi: {menor}')


# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]}... na posição {cont}')
# print('Comi pra caramba!')
