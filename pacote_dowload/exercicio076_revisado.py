papelaria = 'Lapis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,\
    'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90
print('-' * 46)
print(f'{"LISTAGEM DE PREÇO":^45}')
print('-' * 46)
for i in range(0, len(papelaria)):
    if i % 2 == 0:
        print(f'{papelaria[i]:.<37}', end='')
    else:
        print(f'R$ {papelaria[i]:>6.2f}')
