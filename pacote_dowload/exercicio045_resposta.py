# JOKENPO

# IMPORTANTE - EU NÃO SABIA FAZER ISSO!!
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
# print(f"O computador escolheu {(itens[computador])}")

# dados de entrada
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

# frescurinha de tempo
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)

print('-=' * 11)
print(f'Computador jogou {(itens[computador])}')
print(f'Jogador jogou {itens[jogador]}')
# from time import sleep
print('-=' * 11)

# fazer um esqueleto das condicionais
if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 1:  # # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada INVÁLIDA')

elif computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada INVÁLIDA')
