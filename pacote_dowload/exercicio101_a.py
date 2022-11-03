from datetime import date


def voto(a):
    print('-' * 20)
    atual = date.today().year
    idade = atual - a
    if 18 <= idade <= 69:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif 16 <= idade <= 17:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    elif idade >= 70:
        print(f'Com {idade} anos: VOTO FACULTATIVO')
    else:
        print(f'Com {idade} anos: NÃO VOTA')


# Programa principal
num = int(input('Em que ano você nasceu? '))
voto(num)
