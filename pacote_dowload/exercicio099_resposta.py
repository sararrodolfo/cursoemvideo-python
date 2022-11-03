from time import sleep


def maior(*num):
    cont = mai = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.1)
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor foi {mai}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
