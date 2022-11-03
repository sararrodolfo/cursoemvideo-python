validador = 5
while validador == 5:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    print('O que você gostaria de fazer com eles?')

    menu = int(input('[1] somar\n'
                     '[2] multiplicar\n'
                     '[3] maior\n'
                     '[4] novos números\n'
                     '[5] sair do programa\n'
                     'Digite a opção: '))
    if menu == 1:
        print('SOMA')
        print(f'{num1} + {num2} = {num1 + num2}')
    elif menu == 2:
        print('MULTIPLICAÇÃO')
        print(f'{num1} * {num2} = {num1 * num2}')
    elif menu == 3:
        print('MAIOR')
        maior = num1
        if num2 > maior:
            maior = num2
            print(f'Entre {num1} e {num2}, o maior número é {maior}')
        elif num1 == num2:
            print('Não há maior, ambos tem o mesmo valor.')
    elif menu == 4:
        print('NOVOS NÚMEROS')
        num1 = int(input('Digite o novo número: '))
        num2 = int(input('Digite o novo segundo número: '))
        print('O que você quer fazer com eles?')
        menu = int(input('[1] somar\n'
                         '[2] multiplicar\n'
                         '[3] maior\n'
                         '[4] novos números\n'
                         '[5] sair do programa\n'
                         'Digite a opção: '))
        if menu == 1:
            print('SOMA')
            print(f'{num1} + {num2} = {num1 + num2}')
        elif menu == 2:
            print('MULTIPLICAÇÃO')
            print(f'{num1} * {num2} = {num1 * num2}')
        elif menu == 3:
            print('MAIOR')
            if num1 == num2:
                print('Não há maior, ambos tem o mesmo valor')
            elif num1 > num2:
                print(f'Entre {num1} e {num2}, o maior número é {num1}')
            else:
                print(f'Entre {num1} e {num2}, o maior número é {num2}')
        elif menu == 5:
            print("Saindo do programa")
            menu = validador
    elif menu == 5:
        print('Você deseja realmente sair? [S/N]')
        resposta = str(input('Digite sua opção: [S/N] ')).strip().upper()
        if resposta == 'S':
            validador += 1
            print('Obrigada por usar nosso programa. Volte Sempre!')
