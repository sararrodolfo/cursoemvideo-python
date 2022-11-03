from math import factorial
num = int(input('Digite um valor: '))
print(f'O fatorial de {num} é {factorial(num)}')
print(f'Porém, fazendo toda aquela conta é assim: ')
print(f'O fatorial de {num}! = {num}', end=' ')
for n in range(num - 1, 0, -1):
    print(f'x {n}', end=' ')
print(f'= {factorial(num)}')
