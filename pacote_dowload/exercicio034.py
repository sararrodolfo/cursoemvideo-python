""" Desafio 034
Faça um programa que pergunte o salário de um funcionário e
pergunte o valor do seu aumento
Para salários R$ 1250, - aumento de 10%
abaixo disso - aumento 15%
Salário de R$ 1.000,00"""

# Aumento de salário
salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250.00:
    aumento_2 = salario * 1.15
    print(f'Quem ganhava R$ {salario:.2f}, passa a ganhar R$ {aumento_2:.2f}.')
else:
    aumento_1 = salario * 1.1
    print(f'Quem ganhava R$ {salario:.2f}, passa a ganhar R$ {aumento_1:.2f}.')


