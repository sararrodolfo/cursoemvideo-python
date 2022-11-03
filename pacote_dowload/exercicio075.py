"""Desafio 075 - TUDO ERRAOD!
Desenvolva um programa que leia 4 numeros
guarde-os numa tupla
Mostre:
a) quantas vezes apareceu o número 9
b) em que posição foi digitado o primeiro valor 3
c) quais foram os números pares
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
valores = n1, n2, n3, n4
print(f'Os numeros digitados foram: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vez(es).')
print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição.')
print(f'Os valores pares digitados foram: ', end='')
cont = 0
for pares in valores:
    if valores[cont] % 2 == 0:
        print(valores[cont], end=' ')
        cont += 1
    else:
        cont += 1
