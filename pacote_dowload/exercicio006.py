"""Desafio 006 - dobro, triplo e raiz quadrada
leia um número
mostre o seu dobro, triplo e raiz quadrada
"""
# RESPOSTAS
# dobro = a * 2
# triplo = a * 3
# # raiz_quadrada = a * (1/2)  # errado
# raiz_quadrada = a ** (1/2)
# print(f'O valor do dobro é {dobro}, o valor do triplo é {triplo} e a raiz quadrada é {raiz_quadrada:.2f}')
# print(f'O valor do dobro é {a * 2}, o valor do triplo é {a * 3} e a raiz quadrada é {a ** (1/2):.2f}')

# USANDO PARA CORES
# TITULO DO PROGRAMA
print('\33[4;97;44m-----\33[m' * 13)
mensagem = 'OPERAÇÕES MATEMÁTICAS: DOBRO, TRIPLO, RAIZ QUADRADA'
print(f'\33[1;35;107m{mensagem: ^65}\33[m')
print('\33[4;97;44m-----\33[m' * 13)

a = int(input('\33[1;35;107mDigite um valor: \33[m'))


print(f'\33[1;35;107mO valor do \33[m\33[7mdobro\33[m\33[1;35;107m é \33[m\33[1;97;44m{a * 2}\33[m \n'
      f'\33[1;35;107mo valor do \33[m\33[7mtriplo\33[m\33[1;35;107m é \33[m\33[1;97;44m{a * 3}\33[m \n'
      f'\33[1;35;107me a \33[m\33[7mraiz quadrada\33[m\33[1;35;107m é \33[m\33[1;97;44m{pow(a, 1/2):.2f}\33[m')
