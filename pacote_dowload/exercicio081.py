"""Desafio 081
Crie um programa que vai ler vários números e colocar numa lista
Depois disso mostre:
a) Quantos números foram digitados
b) a lista ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista
"""
numeros = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    opcao = ' '
    while opcao not in 'NS':
        opcao = str(input('Quer continuar? [s/n]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Você digitou: {len(numeros)} elemento(s).')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente: {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')
