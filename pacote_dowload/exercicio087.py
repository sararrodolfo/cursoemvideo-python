"""Desafio 087
Aprimorar o 86, mostrando no final:
a) a soma dos valores pares
a) soma dos valores da terceira coluna
c) o maior valor da segunda linha
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma = maior = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print(30 * '-=')
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(30 * '-=')
for l in range(3):
    for c in range(3):
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
for c in range(3):
    soma += matriz[c][2]
for l in range(3):
    for c in range(3):
        maior = matriz[1][c]
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {soma}.')
print(f'O maior valor da segunda linha é {maior}.')