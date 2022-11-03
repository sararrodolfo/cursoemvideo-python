from random import randint

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue advinhar qual foi?')
palpite = int(input('Qual o seu palpite? '))
computador = randint(0, 10)
cont = 0
while palpite != computador:
    if palpite > computador:
        print('Menos, tente outra vez...')
        palpite = int(input('Qual o seu palpite? '))
        cont += 1
    else:
        cont += 1
        print('Mais, tente outra vez...')
        palpite = int(input('Qual o seu palpite? '))

print(f'Acerto ou com {cont} tentativas. Parabéns!')
