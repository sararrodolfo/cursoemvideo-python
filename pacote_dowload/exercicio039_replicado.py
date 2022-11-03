# acrescentando o gênero como condição inicial

from datetime import date

ano_atual = date.today().year

genero = int(input('Informe seu gênero: \n'
                   '1 - FEMININO (mulheres) \n'
                   '2 - MASCULINO (homens) \n'
                   'Digite a opção: '))
lista = [1, 2]
if genero == 1:
    print('Você se identificou sendo do gênero FEMININO.')
    print('O alistamento obrigatório é apenas para homens.')
    print('Informe-se sobre a possibilidade de alistamento facultativo. Boa sorte!')
else:
    print('Você se identificou sendo do gênero MASCULINO.')
    print('Vamos analisar seu caso:')

if genero == 2:
    nascimento = int(input('Informe o ano do seu nascimento: '))
    idade = ano_atual - nascimento
    if idade == 18:
        print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')
        print('Você ainda não tem 18 anos para o alistamento.')
        ano = ano_atual + saldo
        print(f'Ainda falta(m) {saldo} ano(s) para o alistamento.')
        print(f'Seu alistamento será em {ano}.')
    elif idade > 18:
        saldo = idade - 18
        print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')
        print(f'Você já deveria ter se alistado há {saldo} ano(s).')
        ano = ano_atual - saldo
        print(f'Seu alistamento foi em {ano}.')
