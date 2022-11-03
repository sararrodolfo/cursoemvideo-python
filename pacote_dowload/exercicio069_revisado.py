"""Quantas pessoas tem mais de 18 anos
quantos homens foram cadastrados
quantas mulheres tem menos de 20 anos"""
cont = totmaior = tothomem = totmulher = 0
while True:
    print('-==' * 20)
    print(f'{"CADASTRE UMA PESSOA":^45}')
    print('-==' * 20)
    idade = int(input('Idade: '))
    if idade > 18:
        totmaior += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Opção inválida. Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        tothomem += 1
    elif sexo == 'F':
        if idade < 20:
            totmulher += 1
    print('-==' * 20)
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while opcao not in 'SN':
        print('Opção inválida. Quer continuar? [S/N]: ')
    if opcao == 'N':
        break
print('-==' * 20)
print(f'Total de pessoas com mais de de 18 anos: {totmaior}')
print(f'Ao todo temos {tothomem} homem(ns) cadastrado(s).')
print(f'E temos {totmulher} mulher(es) com menos de 20 anos.')
