"""Desafio 056 - é o mais difícil
Desenvolva um programa que leia, nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- a média de idade do grupo
- qual é o nome do homem mais velho
- quantas mulheres tem menos de 20 anos
"""
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    nome = str(input(f'Digite o nome da {p}a. pessoa:  ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} menores de 20 anos no grupo.')
