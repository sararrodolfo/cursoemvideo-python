
"""
Desafio 086
Crie um programa que crie uma matriz de dimensão 3 x3
0, 1, 2 de linha
0, 1, 2 de coluna
preencha com valores lidos pelo teclado
No final, mostre a matriz na tela, com a formatação correta
1, 4, 7 é a primeira coluna
2 5 8 é a segunda coluna
3 6 9 é a terceira coluna
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):  # for de linha
    for c in range(0, 3):  # for de coluna
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print(30 * '-=')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()