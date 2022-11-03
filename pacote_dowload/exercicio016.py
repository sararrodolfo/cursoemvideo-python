# Desafio 016
# leia um número real
# mostre a sua porção inteira
# Exemplo: digite um númer: 6127. O número 6127 tem a parte inteira 6 (math.ceil = arredondamento)

# import math
# real = float(input('Digite um número: '))
# print(f'O número {real:.0f} tem a parte inteira {math.floor(real)}')

# from math import trunc
# real = float(input('Digite um número: '))
# print(f'O número {real:.0f} tem a parte inteira {trunc(real)}')

# Para não ter que importar a biblioteca math
real = float(input('Digite um número: '))
print(f'O número {real} tem a parte inteira {int(real)}')