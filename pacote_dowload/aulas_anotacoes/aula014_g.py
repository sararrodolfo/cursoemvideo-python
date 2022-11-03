"""Laço dentro de um laço"""

x = 0  # coluna
while x < 10:
    y = 0

    while y < 5:
        print(f'{x}, {y}')
        y += 1
    x += 1

print('Acabou')
