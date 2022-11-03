"""
Desafio 094
Crie um programa que leia o nome, idade e sexo de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
a) quantas pessoas foram cadastradas
b) a média da idade do grupo
c) uma lista com todas as mulheres
d) uma lista com pessoas acima da média
"""
dados = []
feminino = []
cadastro = {}
soma = 0
while True:
    cadastro['Nome'] = str(input('Nome: '))
    cadastro['Sexo'] = str(input('Sexo [M/F]: '))
    while cadastro['Sexo'] not in 'MmFf':
        cadastro['Sexo'] = str(input('Sexo [M/F]: '))
    cadastro['Idade'] = int(input('Idade: '))
    soma += cadastro['Idade']
    if cadastro['Sexo'] in 'Ff':
        feminino.append(cadastro['Nome'])
    dados.append(cadastro.copy())
    resp = str(input('Quer continuar? [S/N]: ')).strip()
    if resp in 'Nn':
        break
media = soma / len(dados)
print('-=' * 30)
print(f'O grupo tem {len(dados)} pessoa(s).')
print(f'A média de idade é de {media:.2f} anos')
print(f'As mulheres cadastradas foram: ', end='')
for m in feminino:
    print(f'{m}', end=' ')
print()
if cadastro['Idade'] >= media:
    for k, v in cadastro.items():
        print(f'{k} = {v}', end=' ')
print()
print('<< ENCERRADO >>')
