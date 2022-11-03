"""Desafio 055
Faça um programa que leia o peso de 5 pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""

maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoa}a. pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}')
print(f'O menor peso é {menor}')