"""DESAFIO 38 - COMPARANDO NÚMEROS
Escreva um programa que leia dois números inteiros e
compare-os, mostrando na tela:
define um múmero como maior
- o primeiro valor é maior
- o segundo valor é menor
- não existe valor maior, os dois são iguais"""

# IMPORTANDO APENAS O MÉTODO SLEEP DA CLASSE TIME
from time import sleep

# CRIANDO UM TÍTULO - DO ZERO
print('\33[1;31;107m<3 . <3 . \33[m' * 8)
titulo = 'COMPARANDO NÚMEROS'
print(f'\33[1;36;107m{titulo: ^80}\33[m')
print('\33[1;31;107m<3 . <3 . \33[m' * 8)

# ENTRADA DE VALORES
numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite outro valor: '))

# MENSAGEM
mensagem = 'COMPARANDO OS NÚMEROS'
print(f'\33[0;30;107m{mensagem: ^80}\33[m')

# UTILIZAÇÃO DO MÉTODO IMPORTANTO (ESPECÍFICO)
sleep(2)

# SAÍDA
print(f'Segundo os números digitados, {numero1} e {numero2}, temos que:')
if numero1 > numero2:
    print(f'O valor maior é o {numero1}')
elif numero2 > numero1:
    print(f'O valor maior é {numero2}')
else:
    print('Não temos número maior ou menor, ambos são iguais.')
