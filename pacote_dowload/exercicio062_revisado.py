termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print(f'{termo} ->', end=' ')
soma = cont = 0
while True:
    if cont == 0:
        for c in range(cont, razao):
            if cont == 0:
                soma = razao + termo
                print(f'{soma} ->', end='')
                cont += 1
            else:
                if cont < razao:
                    soma = soma + razao
                    cont += 1
                    print(f'{soma} -> ', end='')
        print('Acabou!')
    else:
        resp = int(input('Deseja mais termos? Quantos? 0 para nenhum termo: '))
        if resp == 0:
            print('Programa encerrado. Volte sempre!')
            break
        else:
            for c in range(0, resp):
                if c < resp:
                    soma = soma + razao
                    print(f'{soma} -> ', end='')
            print('Acabou!')
