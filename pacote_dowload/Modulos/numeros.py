# Programa principal
# from uteis import fatorial, dobro - não é tão indicado para não haver conflito
# from random import randint - módulo, função
# tivemos vários exemplos
import uteis
num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
