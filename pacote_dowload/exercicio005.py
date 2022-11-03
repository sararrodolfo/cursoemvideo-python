"""ANTECESSOR E SUCESSOR
Faça um programa que leia um número inteiro e
mostre na tela o seu sucessor e seu antecessor"""

# COMEÇAR A USAR COMO BASE A MENSAGEM INICIAL

# importando
from time import sleep

# USANDO PARA CORES
# TITULO DO PROGRAMA
print('\33[1;30;43m*****\33[m' * 13)
mensagem = 'OPERAÇÕES ARITMÉTICAS: ANTECESSOR E SUCESSOR'
print(f'\33[1;33;107m{mensagem: ^65}\33[m')
print('\33[1;30;43m*****\33[m' * 13)

# DADOS DE ENTRADA
n = int(input('\33[1;33;107mDigite um número: \33[m'))
print('\33[1;30;43mAnalisando o valor digitado...\33[m')
sleep(2)

# CALCULOS
sucessor = n + 1
antecessor = n - 1

# SAÍDA
print(f'\33[1;30;43mO valor\33[m\33[1;33;107m{n}\33[m\33[1;30;43m, tem por seu: \33[m\n'
      f'\33[1;30;43m== antecessor:\33[m\33[m\33[1;33;107m {antecessor} \33[m\n'
      f'\33[1;30;43m== sucessor:\33[m\33[m\33[1;33;107m {sucessor} \33[m ')