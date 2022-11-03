from random import randint
from time import sleep
computador = randint(0, 5)  # Entre 0 e 5 - simula o que o computador "PENSA"
print('-=-' * 20)
print('Vou pensar num número. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))  # Jogador tenta advinhar, não dá erro colocando spc no final
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')
print("== Fim ==")