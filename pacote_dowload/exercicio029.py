"""Desafio 029 - Radar eletrônico
Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado
A multa vai custar R$ 7,00 por cada km acima do limite
SE ele estiver com 50, não volta nada
Se eu passar a 90km/h, passei 10km, sendo 7 por quilometro = 70 reais
"""

velocidade = int(input('Qual a velocidade atual do carro? '))
limite_u = velocidade - 80  # Calcula a qtdade de quilometros a mais
multa = 7 * limite_u  # Calcula o valor da multa
if velocidade >= 80:
    print("Considerando que o limite de velocidade é de 80km/h...")
    print(f'Você ultrapassou este limite em {limite_u}km/h e será multado em R$ {multa:.2f}.')
    print("Dá próxima vez fique atento ao limite de velocidade para não levar multa!")
else:
    print('Tenha um bom dia! Dirija com segurança!')
print('=== Fim ===')
