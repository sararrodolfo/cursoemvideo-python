"""DESAFIO 065
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução mostre a média entre todos os valores e qual foi
o maior e o menor valores lidos. O programa deve perguntar se o usuário
se ele quer ou não digitar valores.
Quer continuar? Não
Tem que saber a quantidade de valores para saber a média
Qual a média (10 números)
"""
num = 0
soma = 0
cont = 0
opcao = 0
media = 0
maior = 0
acumulador = 0
menor = 0
flag = -1
while opcao != flag:
    num = int(input('Digite um número: '))
    acumulador = num
    cont += 1
    if menor < acumulador:
        menor = acumulador
    if num > maior:
        maior = num
    soma += num
    media = soma / cont
    print('Você deseja mais números?')
    print('[0] para Sim e [-1] para Não')
    opcao = int(input('Digite sua opção: '))
    flag = -1
    while opcao != flag:
        num = int(input('Digite um número: '))
        cont += 1
        soma += num
        media = soma / cont
        if num < acumulador:
            acumulador = num
        else:
            menor = acumulador
        if num > maior:
            maior = num
        print('Você deseja mais números?')
        print('[0] para Sim e [-1] para Não')
        opcao = int(input('Digite sua opção: '))
else:
    print(f'Foram digitados {cont} numero(s).')
    print(f'A média do(s) número(s) digitado(s) foi {media:.2f}')
    print(f'O maior número digitado foi {maior}.')
    print(f'O menor número digitado foi {menor}.')
