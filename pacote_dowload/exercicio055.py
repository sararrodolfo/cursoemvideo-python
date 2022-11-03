"""Desafio 055
Faça um programa que leia o peso de 5 pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""

n1 = float(input('digite o peso 1:'))
n2 = float(input('digite o peso 2: '))
n3 = float(input('digite o peso 3: '))
n4 = float(input('digite o peso 4: '))
n5 = float(input('digite o peso 5: '))
print(n1, n2, n3, n4, n5)
menor = n1
if n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
    menor = n2
if n3 < n2 and n3 < n1 and n3 < n4 and n3 < n5:
    menor = n3
if n4 < n3 and n4 < n2 and n4 < n1 and n4 < n5:
    menor = n4
if n5 < n4 and n5 < n3 and n5 < n2 and n5 < n1:
    menor = n5
print(menor)
maior = n1
if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    maior = n2
if n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    maior = n3
if n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    maior = n4
if n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
    maior = n5
print(maior)