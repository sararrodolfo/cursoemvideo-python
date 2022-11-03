"""DESAFIO 058
Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número
entre 0 e 10
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
'O número que você pensou foi 3?
Resposta: Não
'O número que você pensou foi 5?
Resposta: Não
'O número que você pensou foi 7?
Resposta: Sim
'Parabéns, você acertou, mas foram necessárias 2 tentativas para você acertar"
"""

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar num número. Tente advinhar...')
print('-=-' * 20)
sleep(2)
contador = 0
jogador = ['S', 'N']
while jogador != 'S':
    computador = randint(0, 10)  # Entre 0 e 10 - simula o que o computador "PENSA"
    print(f'Você pensou no número {computador}?')
    print('Resposta: Sim ou Não [S/N]')
    jogador = str(input('[S]im ou [N]ão: ')).strip().upper()
    if jogador == 'N':
        print(f'Você respondeu que [{jogador}]ão.')
        print('Você ERROU! Vou te dar mais uma chance...')
    contador += 1
else:
    contador -= 1
    if contador == 0:
        print('Parabéns, acertou logo de primeira!')
    else:
        print(f'Parabéns! Você acertou, mas foram necessárias {contador} tentativa(s) para acertar!')
