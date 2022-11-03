"""Desafio 064
Faça um programa que leia nome e peso de várias pessoas
guardando tudo numa lista
No final mostre:
a) quantas pessoas foram cadastradas
b) uma listagem com as pessoas mais pesadas
c) uma listagem com as pessoas mais leves
"""
galera = list()
dados = list()
maior = menor = 0
maispesada = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    galera.append(dados[:])
    dados.clear()
    opcao = str(input('Quer continuar? [s/n]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Ao todo você cadastrou {len(galera)} pessoas.')
for c in range(len(galera)):
    if c == 0:
        maior = menor = galera[c][1]
    else:
        if galera[c][1] >= maior:
            maior = galera[c][1]
        if galera[c][1] <= menor:
            menor = galera[c][1]
print(f'O maior peso foi de {maior}Kg. Peso de: ', end='')
for i, v in enumerate(galera):
    if maior == v[1]:
        print(f'{[ v[0] ]}', end=' ')
print(f'\nO menor peso foi de {menor}kg de: ', end='')
for i, v in enumerate(galera):
    if menor == v[1]:
        print(f'{[ v[0] ]}', end=' ')