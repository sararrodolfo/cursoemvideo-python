# Desafio 018
# leia um angulo qualquer (45)
# mostre o valor do seno, cosseno e tangente desse ângulo

# import math
# angulo = float(input('Digite um ângulo: '))
# seno = math.sin(math.radians(angulo))
# print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
# cosseno = math.cos(math.radians(angulo))
# print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
# tangente = math.tan(math.radians(angulo))
# print(f'O angulo de {angulo} tem a TANGENTE de {tangente:.2f}')

# Lembrando que importando apenas essas funções, tem que tirar a menção a math
from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O angulo de {angulo} tem a TANGENTE de {tangente:.2f}')
