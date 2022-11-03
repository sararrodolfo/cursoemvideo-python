"""DESAFIO 41 - ATLETAS
... precisa de um programa que leia o ano de nascimento de um atleta e mostre:
até 9 anos: mirim
até 14: infantil
até 19 anos: junior
até 20 anos: sênior
acima: master
"""

# A LÓGICA DESSE EXERCÍCIO É
# SE UMA CONDIÇÃO FOI PREENCHIDA, NÃO TEM PORQUE SER ENTRE UMA E OUTRA FAIXA DE IDADE

# IMPORTAÇÃO DO ANO ATUAL
from datetime import date

# ENTRADA
nascimento = int(input('Digite o ano de nascimento:  '))

# ANO ATUAL
ano_atual = date.today().year

# CALCULO DA IDADE
idade = ano_atual - nascimento

# CONDIÇÕES
if idade <= 9:
    print(f'Ano de nascimento: {nascimento}')
    print(f'O atleta tem {idade} anos')
    print('Classificação: MIRIM')
# A PARTIR DAQUI NÃO PRECISA DA CONDIÇÃO ABAIXO:
# elif idade >= 9 and idade < 14:
elif idade <= 14:
    print(f'Ano de nascimento: {nascimento}')
    print(f'O atleta tem {idade} anos.')
    print('Classificação: INFANTIL')
elif idade <= 19:
    print(f'Ano de nascimento: {nascimento}')
    print(f'O atleta tem {idade} anos')
    print('Classificação: JUNIOR')
elif idade <= 25:
    print(f'Ano de nascimento: {nascimento}')
    print(f'O atleta tem {idade} anos.')
    print('Classificação: SÊNIOR')
else:
    print(f'Ano de nascimento: {nascimento}.')
    print(f'O atleta tem {idade} anos.')
    print('Classificação: MASTER')