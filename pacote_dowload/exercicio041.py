"""DESAFIO 41 - ATLETAS
... precisa de um programa que leia o ano de nascimento de um atleta e mostre:
até 9 anos: mirim
indo
até 14: infantil
indo
até 19 anos: junior
indo
até 20 anos: sênior
indo
acima: master
"""

# IMPORTAÇÃO DO ANO ATUAL
from datetime import date

# ENTRADA
nascimento = int(input('Digite o ano de nascimento:  '))

# ANO ATUAL
ano_atual = date.today().year

# CALCULO DA IDADE
idade = ano_atual - nascimento

# CONDIÇÕES
if idade < 9:
    print(f'Ano de nascimento: {nascimento}')
    print(f'O atleta tem {idade} anos')
    print('Classificação: Mirim')
elif idade >= 9 and idade < 14:
    print(f'Ano de nascimento: {nascimento}')
    print(f'O atleta tem {idade} anos.')
    print('Classificação: Infantil')
elif idade >= 14 and idade < 19:
    print(f'Ano de nascimento: {nascimento}')
    print(f'O atleta tem {idade} anos')
    print('Classificação: Junior')
elif 19 >= idade < 20:
    print(f'Ano de nascimento: {nascimento}')
    print(f'O atleta tem {idade} anos.')
    print('Classificação: Sênior')
elif idade >= 20:
    print(f'Ano de nascimento: {nascimento}')
    print(f'O atleta tem {idade} anos.')
    print('Classificação: Master')
