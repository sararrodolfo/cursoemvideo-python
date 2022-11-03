a = [2, 3, 4, 7]
# cria uma ligação entre a e b - não é uma cópia
# b = a
"""
Lista A: [2, 3, 4, 7]
Lista B: [2, 3, 4, 7]
"""
# cópia dos valores sem criar uma ligação
b = a[:]  # cópia dos valores de a
"""
Lista A: [2, 3, 4, 7]
Lista B: [2, 3, 8, 7]
"""
b[2] = 8
"""
Lista A: [2, 3, 8, 7]
Lista B: [2, 3, 8, 7]
"""
print(f'Lista A: {a}')
print(f'Lista B: {b}')
