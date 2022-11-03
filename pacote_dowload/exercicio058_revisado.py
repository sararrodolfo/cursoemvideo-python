from random import randint
from time import sleep
computador = randint(0, 10)
print('Tente advinhar o número que eu estou pensando...')
jogador = int(input('Qual o seu palpite entre 0 e 10: '))
print('Vamos ver se você acertou...')
sleep(0.5)
cont = 0
while jogador != computador:
    if jogador > computador:
        print('Menos... Você errou... Tente novamente...')
        jogador = int(input('Digite novo palpite: '))
        cont += 1
    else:
        print('Mais... Você errou... Tente novamente...')
        jogador = int(input('Digite novo palpite: '))
    if jogador == computador:
        print('Parabéns, você acertou.')
print(f'Foram necessária(s) {cont} tentativas...')
