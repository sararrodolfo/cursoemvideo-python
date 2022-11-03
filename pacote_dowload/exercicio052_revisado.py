"""Desafio 052
Faça um programa que leia um número inteiro e diga
se ele é ou não um número primo.
número primo é divísivel por 1 e por ele mesmo.
Só por 1 e por ele mesmo, por nenhum número do intervalo
ele é divisível"""

numero = int(input('Digite um número: '))
tot = 0
for n in range(1, numero + 1):
    if numero % n == 0:  # se o número divisível pelo número do intervalo
        tot += 1
print(f'O número divisível por {tot} vez(es).')
if tot == 2:  # se for 1 e ele mesmo
    print('O número digitado é primo.')
else:
    print('O número digitado não é primo.')
