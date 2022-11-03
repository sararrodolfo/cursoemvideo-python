"""Desafio 032
Faça um programa que leia um ano qualquer e mostre se ele é bissexto"""

# Resposta possível
# não sei a data atual
n = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
b = n % 4
if b == 0:
    print('O ano analisado é um ano bissexto')
else:
    print('O ano analisado não é bissexto')

