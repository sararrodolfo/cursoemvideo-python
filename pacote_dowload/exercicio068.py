"""Par ou Impar
faça um programa que jogue par ou impar com o comoutador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo"""

from random import randint
print('VAMOS JOGAR PAR OU IMPAR')
s = v = 0
while True:
    n = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = n + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Digite [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {n} e o computador jogou {computador}, total de {total}', end=' ')
    if total % 2 == 0:
        print('-> DEU PAR')
        if tipo in 'P':
            v += 1
            print('Você venceu...')
            print('Vamos jogar novamente...')
        else:
            print('==-==' * 5)
            print('VOCÊ PERDEU!')
            print('==-==' * 5)
            print(f'GAME OVER! Você venceu {v} vezes.')
            break
    elif total % 2 != 0:
        print('-> DEU IMPAR')
        if tipo in 'I':
            v += 1
            print('Você venceu...')
            print('Vamos jogar novamente...')
        else:
            print('==-==' * 5)
            print('VOCÊ PERDEU!')
            print('==-==' * 5)
            print(f'GAME OVER! Você venceu {v} vezes.')
            break
