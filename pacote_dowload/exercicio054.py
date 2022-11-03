"""Desafio 054
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas não atingiram a maioridade e quantas já são maiores.
Contador - considere a maioridade 21 anos"""

# primeiro eu tenho que importar o ano atual
from datetime import date

# variável com a data atual
atual = date.today().year

# CONTADOR DE CADA UM - MAIOR E MENOR COMEÇA COM ZER (NÃO É UM SÓ CONTADOR!)
totmaior = 0
totmenor = 0
# AQUI EU INCLUO O INTERVALO
for pess in range(1, 8):

    # incluir o ano de nascimento
    nasc = int(input(f'Em que ano a {pess}a. pessoa nasceu? '))

    # verificar quantos anos a pessoa tem
    idade = atual - nasc

    # saída da idade / ao invés de imprimir a idade, coloca a condição
    # print(f'A pessoa tem {idade} anos')

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'E também tivemos {totmenor} pessoas menores de idade')
