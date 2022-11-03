"""Desafio 031 - Preço da passagem
Crie um programa que pergunte a distância de uma viagem em Km
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de avião
de até 200km e R$ 0,45 para viagens mais longas"""

distancia = int(input('Qual é a distância da sua viagem? '))
if distancia >= 200:
    print(f'Você está prestes a começar uma viagem de {distancia:.1f}km \n'
          f'E o preço da sua passagem será de R$ {distancia * 0.50:.2f}')
else:
    print(f'Você está prestes a começar uma viagem de {distancia:.1f}km \n'
          f'E o preço da sua passagem será de R$ {distancia * 0.45:.2f}')
print('Fim')
