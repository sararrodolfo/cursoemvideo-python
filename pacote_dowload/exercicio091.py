"""
Desafio 091
Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário. No final, coloque
em ordem, sabendo que o vencedor tirou o maior número no dado.
randint
4 elementos
vai sortear para cada um deles
sleep
"""
from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
print('Valores sorteados:')
print('-' * 30)
for c in range(0, 4):
    jogadores[c+1] = randint(1, 6)
for k, v in jogadores.items():
    print(f'O jogador{k} tirou {v}')
    sleep(0.5)
print('Ranking dos jogadores:')
print('-' * 30)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: jogador/tirou {v}')