"""Crie um programa que leia dois números e
mostre a soma entre eles"""
print('\33[1;36;107m-==\33[m' * 13)
mensagem = "SOMANDO VALORES"
print(f'\33[1;36;107m{mensagem: ^39}\33[m')
print('\33[1;36;107m-==\33[m' * 13)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print(f'\33[1;97;46mA soma entre {n1} + {n2} é de {n1 + n2}\33[m')
