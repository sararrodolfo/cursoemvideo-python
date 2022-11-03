"""Desafio 078
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
No final, mostre qual foi o maior e o menor valor digitado e as
suas respectivas posições na lista
"""
valores = list()
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
# for c, v in enumerate(valores):
#     if c == 0:
#         maior = v
#         posmaior.append(c)
#         menor = v
#         posmenor.append(c)
#     else:
#         if v >= maior:
#             maior = v
#             if maior == v:
#                 posmaior.append(c)
#             else:
#                 posmaior.pop(c)
#         if v <= menor:
#             menor = v
#             if menor == v:
#                 posmenor.append(c)
#             else:
#                 posmenor.pop(c)
print('-==-' * 10)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi o {maior} na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi o {menor} na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')

