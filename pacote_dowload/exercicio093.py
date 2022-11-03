"""
Desafio 093
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai
ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols
feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato.
"""
jogador = dict()
gols = []
jogador['Nome'] = str(input('Nome do jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {c + 1}? '))
    gols.append(gol)
jogador['Gols'] = gols
jogador['Total'] = sum(gols)
print(30 * '-=')
print(jogador)
print(30 * '-=')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(30 * '-=')
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for k, v in enumerate(gols):
    print(f'    => Na partida {k + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')