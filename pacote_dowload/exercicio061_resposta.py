print('Gerador de PA')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 0
soma = termo
print(f'{soma} -> ', end='')
while contador < 9:
    soma += razao
    contador += 1
    print(f'{soma} -> ', end='')
print('FIM', end='')

