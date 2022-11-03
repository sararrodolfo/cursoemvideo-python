"""Desafio 088
Faça um programa que ajude um jogador da Mega Sena a criar palpites
O programa vai perguntar quantos jogos serão gerados e vai sortear
os números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
composta...
sortear os jogos
tem um sleep entre um jogo e outro
os números vão de 1 a 60
não pode gerar os mesmos números num mesmo jogo - 10, 20, 30, 40, 40, 60
"""
from random import randint

print(30 * '-=')
print(f'{"JOGO DA MEGA SENA":^60}')
print(30 * '-=')
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=--=--=-   SORTEANDO {n} JOGOS   -=--=--=-')
jogo = []
for c in range(0, n):
    jogo.append([randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)])
for c in range(0, n):
    print(f'Jogo {c + 1}: ', end='')
    jogo[c].sort()
    print(jogo[c])
print(f'-=--=--=-   BOA SORTE!   -=--=--=-')
