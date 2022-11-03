'''Deafio 023 - matematicamente ou por string
um número de 0 a 9999
mostre na tela cada um dos dígitos seperados
EXemplo: digite um número: 1834
unidade: 4
dezenas: 3
centenas: 8
milhar: 1'''

# dá erro se não usar os 4 dígitos
# numero = str(int(input('Digite um número: ')))
# print(f'Unidade: {numero[3]}')
# print(f'Dezenas: {numero[2]}')
# print(f'Centenas: {numero[1]}')
# print(f'Milher: {numero[0]}')

# opção 2 = usando // 1

numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando seu número...')
print(f'Unidade: {u}')
print(f'Dezenas: {d}')
print(f'Centenas: {c}')
print(f'Milhar: {m}')
