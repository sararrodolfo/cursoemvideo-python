"""Desafio 079
crie um programa onde o usuário possa digitar vários números
cadastre-os numa lista
caso o número já exista, não será adicionado
no final: exibir todos os valores já digitados em ordem crescente
"""

numeros = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    if numeros[-1] not in numeros[:-1]:
        print("Valor adicionado com sucesso")
    else:
        numeros.pop()
        print('Valor duplicado! Não vou vou adicionar')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Você digitou os valores: {sorted(numeros)}')
