maior = f = m = 0
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    while not int:
        idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]:  ')).strip().upper()[0]
    if sexo in 'F' and idade <= 20:
        f += 1
    else:
        m += 1
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao in 'Nn':
        print(f'Total de pessoas com mais de 18 anos: {maior}.')
        print(f'Ao todo temos {m} homens cadastrados.')
        print(f'E temos {f} mulher(es) com menos de 20 anos.')
        break
