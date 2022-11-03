"""Desafio 049
Refaça o DESAFIO 009 mostrando a tabuada de um número, só que agora utilizando um laço for"""

"""Desafio 009 - TABUADA
leia um número inteiro
mostre a sua tabuada"""

# USANDO PARA CORES
# TITULO DO PROGRAMA
print('\33[1;97;42m --**-- \33[m' * 8)  # inversao cor 31 - vermelho
mensagem = 'OPERAÇÕES MATEMÁTICAS: TABUADA'
print(f'\33[1;36;107m{mensagem: ^64}\33[m')
print('\33[1;97;42m --**-- \33[m' * 8)  # inversao cor 97 - branco

n = int(input('Digite o número da tabuada a pesquisar: '))
print(f'A tabuada do {n} é:')
for c in range(1, 11):
    print(f'{c} x {n} = {c * n}')

# n = int(input('Digite o número da tabuada a pesquisar: '))
# print(f'A tabuado do {n} é:')
# print(f' {n} * 1 = {n * 1} ')
# print(f' {n} * 1 = {n * 2} ')
# print(f' {n} * 1 = {n * 3} ')
# print(f' {n} * 1 = {n * 4} ')
# print(f' {n} * 1 = {n * 5} ')
# print(f' {n} * 1 = {n * 6} ')
# print(f' {n} * 1 = {n * 7} ')
# print(f' {n} * 1 = {n * 8} ')
# print(f' {n} * 1 = {n * 9} ')
# print(f' {n} * 1 = {n * 10} ')

# # ENTRADA
# n = int(input('\33[1;36mDigite o número da tabuada a pesquisar: \33[m'))

# # SAÍDA
# print(f'\33[1;3mA tabuado do {n} é:\33[m')
# print(f'\33[1;36m {n} x {1:2} = {n * 1} \33[m')
# print(f'\33[1;36m {n} x {2:2} = {n * 2} \33[m')
# print(f'\33[1;36m {n} x {3:2} = {n * 3} \33[m')
# print(f'\33[1;36m {n} x {4:2} = {n * 4} \33[m')
# print(f'\33[1;36m {n} x {5:2} = {n * 5} \33[m')
# print(f'\33[1;36m {n} x {6:2} = {n * 6} \33[m')
# print(f'\33[1;36m {n} x {7:2} = {n * 7} \33[m')
# print(f'\33[1;36m {n} x {8:2} = {n * 8} \33[m')
# print(f'\33[1;36m {n} x {9:2} = {n * 9} \33[m')
# print(f'\33[1;36m {n} x {9:2} = {n * 10} \33[m')
