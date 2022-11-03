num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
while True:
    opcao = int(input('''O que gostaria de fazer?
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair
    Opção: '''))
    if opcao == 1:
        print(f'A soma de {num1} + {num2} = {num1 + num2}')
    elif opcao == 2:
        print(f'A muliplicação de {num1} x {num2} = {num1 * num2}')
    elif opcao == 3:
        maior = 0
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior número entre {num1} e {num2} é {maior}')
        if num1 == num2:
            print('Os números são iguais, não há maior.')
    if opcao == 4:
        num1 = int(input('Digite o novo número: '))
        num2 = int(input('Digite o outro número: '))
    if opcao == 5:
        print('Programa enecerrado. Volte sempre.')
        break
