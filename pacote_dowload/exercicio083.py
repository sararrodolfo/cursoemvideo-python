"""Desafio 083
Crie um programa onde o usuário digite uma expressão qualquer
que use parenteses
seu aplicativo deverá analisar se a expressão passada está com os
parenteses abertos e fechados na ordem correta
"""
texto = list()
texto.append(str(input('Digite a expressão: ')).strip())
for letra in texto:
    if letra.count('(') and letra.count(')') % 2 != 0:
        print('Sua expressão está errada!')
    else:
        print('Sua expressão é valida!')
