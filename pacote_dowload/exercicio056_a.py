"""Desafio 056 - é o mais difícil
Desenvolva um programa que leia, nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- a média de idade do grupo
- qual é o nome do homem mais velho
C - quantas mulheres tem menos de 20 anos
RESPOSTA:
A - Média de idade do gripo
B - o nome do homem mais velho
C - MULHERES OK

"""

# importar o ano atual
from datetime import date

# ano atual
atual = date.today().year

# laço para pedir os dados
# pedido de nome
# pedido do ano do nascimento
# pedido do gênero
# condição: menor de 21 anos
# media do grupo
menor = 0
homem_velho = 0
soma_idade = 0
media = 0
mais_velho = 0
nome_mais = ''

for pessoa in range(1, 5):
    nome = str(input(f'Digite o nome da {pessoa}a. pessoa: '))
    nasc = int(input('Digite o ano do seu nascimento: '))
    # somar as idades e obter a média
    idade = atual - nasc
    soma_idade += idade
    media = soma_idade / 4
    sexo = int(input('Informe seu gênero: \n'
                     '1 - para HOMEM\n'
                     '2 - para MULHER\n'
                     'Digite a opção: '))
    if pessoa == 1 and sexo == 1:
        mais_velho = idade
        nome_mais = nome
    if sexo == 2:
        if nasc >= 2000:
            menor += 1

print(f'{nome_mais} é o homem mais velho do grupo.')
print(f'A média de idade do grupo é de {media:.2f} anos.')
print(f'Tem {menor} mulher(es) menor de 21 anos de idade.')
