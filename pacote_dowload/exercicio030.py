"""Desafio 030 - Número par
 Crie um programa que leia um número qualquer e diga se ele é número PAR  ou IMPAR
 lembrando que se o resultado da divisão daquele número - resto - for 0 é porque é par"""

# # tente ser o mais simples possível
# numero = int(input('Digite um número qualquer:'))
# par = (numero / 2)
# if par == 0:
#     print(f'O número que você digitou {numero} é par!')
# print(f'O número digitado não é um número par, ou seja, é ímpar.')

# Um pouco mais complicado
numero = int(input('Digite um número qualquer: '))
par = (numero % 2)
if par == 0:
    print(f'O número que você digitou {numero} é um número par')
print(f'O número digitado não é um número par, ou seja, é impar.')
