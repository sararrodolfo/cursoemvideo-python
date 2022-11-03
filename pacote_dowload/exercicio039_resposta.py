from datetime import date
ano_atual = date.today().year

nascimento = int(input('Digite o ano do nascimento: '))
idade = ano_atual - nascimento

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos para o alistamento. \n'
          f'Ainda faltam {saldo} ano(s). ')
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')
    ano = ano_atual + saldo
    print(f'Seu alistamento será em {ano}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')
    print(f'Você já deveria ter se alistado há {saldo} ano(s).')
    ano = ano_atual - saldo
    print(f'Seu alistamento foi em {ano}.')


"""Dica:
O alistamento apenas para homem
Se for mulher, para ler o sexo"""