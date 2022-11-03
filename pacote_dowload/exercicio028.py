'''Desafio 028
Escreva um programa que faça o computar pensar em um número inteiro entre  0 a 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
O programa deverá escrever na tela se o usuário venceu ou perdeu - lembrei do random
 Exemplo: Pensei no número...'''

# importação de módulos, método específico
from random import choice
from time import sleep

# código
# TITULO
print('--=--' * 15)
print('Vou pensar num número entre 0 e 5. Tente adivinhar...')
print('--=--' * 15)

# NÚMERO DO USUÁRIO
numero = int(input('Em que número eu pensei? '))

# OPÇÕES
opcoes = [0, 1, 2, 3, 4, 5]

# PARECE QUE ESTÁ "PENSANDO"
sleep(1)

# RESPOSTA DO PROGRAMA
resposta = choice(opcoes)

# CONDIÇÃO
if resposta == numero:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! Tente novamente.')
print('== Fim ==')
