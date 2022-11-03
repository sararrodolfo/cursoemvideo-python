print('--==--' * 8)
print(f'{"Sequência de Fibonacci":^45}')
print('--==--' * 8)
n = int(input('Quantos termos gostaria? '))
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → Fim')