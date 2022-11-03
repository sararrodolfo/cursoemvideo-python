"""Desafio 082
Crie um programa que vai ler vários números e colocar numa lista
Depois disso crie duas listas extras, conter valores pares e valores ímpares
digitados respectivamente
Ao final, mostre o conteúdo das tres listas geradas
"""
numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    opcao = ' '
    while opcao not in 'NS':
        opcao = str(input('Quer continuar? [s/n]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'A lista completa é: {numeros}')
for c in range(len(numeros)):
    if numeros[c] % 2 == 0:
        pares.append(numeros[c])
    else:
        impares.append(numeros[c])
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')
