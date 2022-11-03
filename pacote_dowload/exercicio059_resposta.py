validador = True
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
while validador:
    menu = int(input('''
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
        >>>> Qual é a sua opção: '''))
    if menu == 1:
        print('SOMA')
        print(f'{num1} + {num2} = {num1 + num2}')
        print('****' * 10)
    elif menu == 2:
        print('MULTIPLICAÇÃO')
        print(f'{num1} * {num2} = {num1 * num2}')
        print('****' * 10)
    elif menu == 3:
        print('MAIOR')
        maior = num1
        if num2 > maior:
            maior = num2
            print(f'Entre {num1} e {num2}, o maior número é {maior}')
        elif num1 == num2:
            print('Não há maior, ambos tem o mesmo valor.')
        print('****' * 10)
    elif menu == 4:
        print('NOVOS NÚMEROS')
        num1 = int(input('Digite o novo número: '))
        num2 = int(input('Digite o novo segundo número: '))
        print('****' * 10)
    elif menu == 5:
        print('Você deseja realmente sair? [S/N]')
        resposta = str(input('Digite sua opção: [S/N] ')).strip().upper()[0]
        if resposta in 'Ss':
            print('Obrigada por usar nossa calculadora. Volte Sempre!')
            validador = False
        else:
            validador = True
        print('****' * 10)
