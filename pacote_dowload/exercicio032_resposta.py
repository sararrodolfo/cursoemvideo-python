"""Desafio 032
Faça um programa que leia um ano qualquer e mostre se ele é bissexto"""

# Resposta possível
from datetime import date  # para importar a data
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:  # a condição para caso a resposta seja 0
    ano = date.today().year   # aqui vai pegar o ano atual da máquina
# ano tem que ser divisível por 4, não pode ser (!=) )divisivel por 100 e tem que ser divisível por 400
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO É BISSEXTO.')
