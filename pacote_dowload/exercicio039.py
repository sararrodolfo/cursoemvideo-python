"""DESAFIO 39 - ALISTAMENTO
Faça um programa que leia o ano de nascimento de um jovem e
informe, de acordo com a sua idade:
- se ele ainda vai se alistar ao serviço militar
- se é a hora de se alistar
- se já passou do tempo de alistamento
## usar o ano do sistema
Seu programa também deverá mostrar o tempo que falta
ou que passou do prazo"""

# EXERCICIO 032 - IMPORTAR O MÉTODO DATE PARA OBTER O ANO ATUAL
# IMPORTANDO DATE, DA CLASSE DATETIME
from datetime import date

# ENTRADA - ANO DE NASCIMENTO
ano = int(input('Digite o ano de seu nascimento: '))

# ANO ATUAL
ano_atual = date.today().year

# IDADE ATUAL
idade = ano_atual - ano

# SAÍDA
print(f'Você nasceu em {ano}, atualmente tem {idade} anos.')
print(f'De acordo com a sua idade:')
if idade < 18:
    print(f'Ainda falta(m) {18 - idade} ano(s) para o alistamento')
elif idade == 18:
    print(f'É hora do alistamento!')
elif idade > 18:
    print("Já passou da hora do alistamento. \n"
          f"Você deveria ter se alistado em {ano_atual - 18}. \n"
          "Regularize sua situação junto ao Exército.")



# - se é a hora de se alistar
# - se já passou do tempo de alistamento
# ## usar o ano do sistema
# Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo"""