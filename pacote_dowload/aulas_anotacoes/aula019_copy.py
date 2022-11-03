estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())

# Laço para dentro de uma lista
# for e in brasil:
#     for k, v in e.items():
#         print(f'O campo {k} tem valor {v}.')
# O campo uf tem valor Rio.
# O campo sigla tem valor RJ.
# O campo uf tem valor Sao Paulo.
# O campo sigla tem valor SP.
# O campo uf tem valor Goias.
# O campo sigla tem valor GO.

# Laço para dentro de um dicionário
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()