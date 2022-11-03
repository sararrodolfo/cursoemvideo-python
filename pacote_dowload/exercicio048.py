"""Desafio 048
Faça um programa que calcule a SOMA todos os números ímpares
que são múltiplos de 3,
e que se encontram no intervalo de 1 a 500.
divisível"""
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma = soma + c
print(f'A soma de todos os {cont} valores solicitados é: {soma}')
