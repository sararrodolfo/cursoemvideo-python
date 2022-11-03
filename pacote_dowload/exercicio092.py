"""
Desafio 092
Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os
em um dicionário. Se por um acaso a CTPS for diferente de zero, o dicionário receberá
também o ano de contratação e o salário. Calcule e acrescente além da idade, com
quantos anos a pessoa vai se aposentar.
"""
from datetime import date
pessoa = {'Nome': str(input('Nome: ')), 'Idade': int(input('Ano de nascimento: ')),
          'CTPS': int(input('Carteira de trabalho (0 não tem): '))}
ano = date.today().year
pessoa['Idade'] = ano - pessoa['Idade']
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário R$: '))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Contratação']) + 35) - ano
else:
    pessoa['Aposentadoria'] = 35
for k, v in pessoa.items():
    print(f'    => {k} tem o valor {v}')