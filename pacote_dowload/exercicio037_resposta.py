num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

# O PYTHON TEM CONVERSÃO AUTOMÁTICO
if opcao == 1:
    # FATIAMENTO, TIRANDO OS DOIS PRIMEIROS DÍGITOS QUE APARECERIAM 0b indicando que é binário
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')  # FATIAMENTO, TIRANDO OS DOIS PRIMEIROS DÍGITOS
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')  # INDICA QUE É HEX 0X (TIRANDO O OX)
else:
    print(f'OPÇÃO INVÁLIDA. TENTE NOVAMENTE')
