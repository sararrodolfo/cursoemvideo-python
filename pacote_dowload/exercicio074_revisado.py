from random import randint
numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print('Os valores sorteados foram: ', end='')
cont = menor = maior = 0
for n in numeros:
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont += 1
    print(n, end=' ')
print(f'\nO maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')
