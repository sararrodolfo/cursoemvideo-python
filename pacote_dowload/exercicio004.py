""" DISSECANDO UMA VARIÁVEL
Faça um programa que leia algo no teclado e
mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela"""
# valor_input (é um objeto - como tudo no python)
# tem atributos e métodos( str tem tudo isso)"""

# importando módulos
from time import sleep
from emoji import emojize

# USANDO PARA CORES
# TITULO DO PROGRAMA
print('\33[1;97;41m*****\33[m' * 13)
mensagem = 'DISSECANDO UMA VARIÁVEL'
print(f'\33[1;31;107m{mensagem: ^65}\33[m')
print('\33[1;97;41m*****\33[m' * 13)

# valor de entrada
valor = 'Digite algo: '
valor_input = input(f'\33[1;30;107m{valor}\33[m')

# usando aquele tempinho...
print('\33[1;30;107mDissecando o valor digitado...\33[m')
# dando a impressão de que está a analisar
sleep(2)

# DISSECANDO
print(f'\33[1;30;107mO tipo primitivo desse valor é,\33[m \33[1;31;107m{type(valor_input)}\33[m')
sleep(2)
print(f'\33[1;30;107mSó tem espaços?,\33[m \33[1;31;107m{valor_input.isspace()}\33[m')
sleep(2)
print(f'\33[1;30;107mÉ um número?,\33[m \33[1;31;107m{valor_input.isnumeric()}\33[m')
sleep(2)
print(f'\33[1;30;107mÉ alfabético?,\33[m \33[1;31;107m{valor_input.isalpha()}\33[m')
sleep(2)
print(f'\33[1;30;107mÉ alfanumérico?,\33[m \33[1;31;107m{valor_input.isalnum()}\33[m')
sleep(2)
print(f'\33[1;30;107mEstá em maíúscula?,\33[m \33[1;31;107m{valor_input.isupper()}\33[m')
sleep(2)
print(f'\33[1;30;107mEstá em minúsculas?,\33[m \33[1;31;107m{valor_input.islower()}\33[m')
sleep(2)
# não sabia - istittle (é capitalizada)
print(f'\33[1;30;107mEstá capitalizada?,\33[m\33[1;31;107m{valor_input.istitle()}\33[m')

# mensagem final
simbolo = emojize(':thumbs_up: CANSADA! MAS EMPOLGADA! :thumbs_up:', language='alias')
print(f'\33[m \33[1;31;107mUfa...\33[m \33[1;30;107mTrabalhei bastante, né? {simbolo}\33[m')
