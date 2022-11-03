from random import randint

print('-==' * 20)
print(f'{"VAMOS JOGAR PAR OU IMPAR":^55}')
print('-==' * 20)
cont = soma = 0
while True:
    jogador = int(input('Diga um valor: '))
    opcao = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    while opcao not in 'PI':
        opcao = str(input('Opção inválida. Par ou Ímpar [P/I]: ')).strip().upper()[0]
    computador = randint(0, 10)
    print('-==' * 20)
    print(f'Você jogou {jogador} e o computador jogou {computador}. ', end='')
    soma = jogador + computador
    if soma % 2 == 0:
        print('Deu PAR!')
        if opcao == 'P':
            print('Você VENCEU! Vamos jogar novamente...')
            cont += 1
        else:
            print('-==' * 20)
            print('Você PERDEU!')
            print(f'GAME OVER. Você venceu {cont} vez(es)')
            break
    else:
        print('Deu IMPAR')
        if opcao == 'I':
            print('Você VENCEU! Vamos jogar novamente...')
            cont += 1
        else:
            print('-==' * 20)
            print('Você PERDEU!')
            print(f'GAME OVER. Você venceu {cont} vez(es)')
            break