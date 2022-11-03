"""Desafio 101
Crie um programa que tenha um função chamada voto()
que vai receber como parâmetro o ano de nascimento de
uma pessoa e retornando um valor literal indicando
se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
nas eleições
"""


def voto(a):
    from datetime import date  # se eu vou usar só na função, faz a importação aqui
    print('-' * 20)
    atual = date.today().year
    idade = atual - a
    if 18 <= idade <= 69:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Com {idade} anos: VOTO FACULTATIVO'
    else:
        return f'Com {idade} anos: NÃO VOTA'


# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
