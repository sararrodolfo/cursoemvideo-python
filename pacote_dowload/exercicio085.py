"""Desafio 085
Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os numa lista única que mantenha separados
os valores pares
e os valores ímpares
No final, mostre os valores pares e os valores ímpares em ordem crescente
"""
principal = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input(f'Digite o {c + 1}º valor: '))
    if valor % 2 == 0:
        principal[0].append(valor)
    else:
        principal[1].append(valor)
print('-=' * 30)
print(f'Os valores pares digitados foram: {principal[0]}')
print(f'Os valores impares digitados foram: {principal[1]}')
