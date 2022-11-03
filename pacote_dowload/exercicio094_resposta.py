pessoa = dict()
galera = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('[M/F]: '))
        if pessoa['Sexo'] in 'MmFf':
            break
        print('ERRO! Por favor, digite apenas M/F')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S/N')
    if resp == 'N':
        break
print(30 * '-')
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}', end=' ')
print()
for p in galera:
    if p['Idade'] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} =  {v}', end=' ')
        print()
print('<< ENCERRADO >>')