"""Desafio 052
Faça um programa que leia um número inteiro e diga
se ele é ou não um número primo.
número primo é divísivel por 1 e por ele mesmo.
Só por 1 e por ele mesmo, por nenhum número do intervalo
ele é divisível"""


num = int(input('Digite um número: '))
# for c in range(0, num):

# aqui eu errei - deveria ser dividido por 'c' e não pelo num
#     if num % 1 and num % num == 0:
#         print('primo')
#     else:
#         print('n primo')

# mostrar todos os valores do intervalo
# for c in range(1, num + 1):
#     print(f'{c}', end=' ')

tot = 0  # contador - para mostrar quantas vezes foi divisível
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
        print(f'\33[33m', end=' ')  # colocou apenas a formatação de cor
    else:
        print(f'\33[31m', end=' ')  # colocou apenas a formatação de cor
    print(f'{c}', end=' ')  # definiu o que irá se repetir em ambos, pela identação dá para saber
print(f'\n\33[mO número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('E por isso ele é PRIMO.')
else:
    print('E por isso ele NÃO É PRIMO.')