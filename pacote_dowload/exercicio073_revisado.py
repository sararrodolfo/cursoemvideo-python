times = 'Corinthians', 'Atlético-MG', 'Santos', 'Avaí', 'América-MG', 'Palmeiras', 'Bragantino', 'Internacional',\
        'São Paulo', 'Botafogo', 'Fluminense', 'Coritiba', 'Cuiabá', 'Athlético-PR', 'Flamengo', 'Goiás', 'Ceará',\
    'Atlético-GO', 'Fortaleza'
print('-==-' * 10)
print(f'Lista de times do Brasileirão: {times}')
print('-==-' * 10)
print(f'Os cinco primeiros times são {times[0:5]}')
print('-==-' * 10)
print(f'Os quatro últimos são: {times[-4:]}')
print('-==-' * 10)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-==-' * 10)
if 'Chapecoense' in times:
    print(f'A Chapecoense está na posição {times.index("Chapecoense")}')
else:
    print('A Chapecoense não está entre os times do Brasileirão')
