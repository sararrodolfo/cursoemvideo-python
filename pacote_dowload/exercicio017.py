# Desafio 017
# comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo
# calcule e mostre o o comprimento da hipotenusa

# Matematica Formal
# co = float(input('Digite o valor do cateto oposto: '))
# ca = float(input('Digite o valor do cateto adjacente: '))
# hipotenusa = ( ca ** 2 + co **2) ** (1/2)
# print (f'O valor da hipotenusa é: {hipotenusa}')

# Com a importação completa
# import math
# co = float(input('Digite o valor do cateto oposto: '))
# ca = float(input('Digite o valor do cateto adjacente: '))
# hipotenusa = math.hypot(co, ca)
# print(f'O valor da hipotenusa é: {(hipotenusa):.2f}')

# Como vou usar só a hipotenusa
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print(f'O valor da hipotenusa é: {hypot(ca, co):.2f}')
