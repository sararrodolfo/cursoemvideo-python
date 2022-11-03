"""
Desafio 095
Aprimore o exercício 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes de aproveitamento
de cada jogador
"""
campeonato = []
jogador = dict()
gols = []
cont = 0
while True:
    jogador['Nome'] = str(input('Nome do jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {c + 1}? '))
        gols.append(gol)
    jogador['Gols'] = gols
    jogador['Total'] = sum(gols)
    cont += 1
    campeonato.append(jogador.copy())
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"Cód":<4} | {"Gols":<10} | {"Total":<5}')
