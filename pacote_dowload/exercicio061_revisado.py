termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print(f'{termo} ->', end=' ')
cont = soma = 0
while True:
    while cont < 9:
        if cont == 0:
            soma = termo + razao
            cont += 1
        else:
            soma = soma + razao
            cont += 1
        print(f'{soma} -> ', end='')
        if cont == 9:
            print('Acabou!')
    novostermos = int(input('Deseja novos termos? [0] nenhum: '))
    if novostermos == 0:
        print('Programa encerrado. Volte sempre')
        break
    if novostermos != 0:
        cont = 0
        while novostermos > cont:
            soma = soma + razao
            cont += 1
            print(f'{soma} -> ', end='')
        print('Acabou!')
