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
    print(f'Você jogou {n} e o computador jogou {computador}, total de {total}', end=' -> ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
