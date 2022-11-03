media = soma = totmulher = maior = 0
velho = ''
for c in range(0, 4):
    nome = str(input(f'Digite o nome da {c + 1}ª pessoa: ')).strip().upper()
    idade = int(input(f'Digite a idade: '))
    if c == 0:
        maior = idade
    else:
        if idade > maior:
            maior = idade
    soma = soma + idade
    media = soma / 4
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Digite novamente. [M/F]: '))
    if sexo == 'F':
        if idade < 20:
            totmulher += 1
    if sexo == 'M':
        if idade == maior:
            velho = nome

print(f'A média de idade do grupo é de {media:.0f} anos.')
print(f'O nome do homem mais velho é {velho}.')
print(f'A quantidade de mulheres menor de 20 anos é de {totmulher}.')
