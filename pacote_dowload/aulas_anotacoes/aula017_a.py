"""
pode criar uma lista vazia e inserir valores pelo input no for
valores = []
valores = list[]
"""
# valores = [] # está dando o sublinhado porque ele não interpretou que era uma lista
valores = list()
# valores.append(5)
# valores.append(9)
# valores.append(4)
# print(valores)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
"""
Na posição 0 eu encontrei o valor 4!
Na posição 1 eu encontrei o valor 8!
Na posição 2 eu encontrei o valor 9!
Na posição 3 eu encontrei o valor 1!
Na posição 4 eu encontrei o valor 3!
Cheguei ao final da lista.
"""

for c, v in enumerate(valores):
    print(f'Na posição {c} eu encontrei o valor {v}!')
print('Cheguei ao final da lista.')
