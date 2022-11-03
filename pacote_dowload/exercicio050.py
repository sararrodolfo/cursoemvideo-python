"""Desafio 050
Desenvolva um programa que leia 6 (seis) números inteiros e
mostre a soma apenas daqueles que forem pares!
Se o valor digitado for impar, desconsidere-o
ainda pode ser melhorado no print - pode ser adicionada a posição, o que nesse caso
ao invés de ser ZERO como eu fiz inicialmente, coloca o 1 até o 7 -
porque vai até o 6 faz a soma - acumulador partindo do zero (mais o número digitado)
como o contador que parte do zero e vai somando mais um
"""
soma = 0
for n in range(0, 7):
    numero = int(input(f'Digite um número na posição {n}: '))
    if numero % 2 == 0:
        soma = soma + numero
print(f'A soma dos números pares digitados foi {soma}')
