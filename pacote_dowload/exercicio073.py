"""Desafio 073
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
na ordem de colocação
Depois mostre:
a - apenas os 5 primeiros colocados
b - os últimos 4 colocados da tabela
c - uma lista com os times em ordem alfabética
d - em que posição está a Chapecoense
"""

times = 'Corinthians', 'Atlético-MG', 'Santos', 'Avaí', 'América-MG', 'Palmeiras', 'Bragantino', 'Internacional',\
        'São Paulo', 'Botafogo', 'Fluminense', 'Coritiba', 'Cuiabá', 'Athlético-PR', 'Flamengo', 'Goiás', 'Ceará',\
    'Atlético-GO', 'Fortaleza'
print("**-**" * 10)
print(f'Lista de times do Brasileirão: {times}')
print("**-**" * 10)
print(f'Os 5 primeiros são: {times[0:5]}')
print("**-**" * 10)
print(f'Os 4 últimos são: {times[15:19]}')
print("**-**" * 10)
print(f'Times em ordem alfabética: {sorted(times)}')
print("**-**" * 10)
# print(times.index("Chapecoense"))
# print(times.count('Chapecoense'))
if 'Chapecoense' in times:
    print(f'A Chapecoense está na posição {times.index("Chapecoense")}')
else:
    print(f'A Chapecoense não está na lista dos 20 times do Brasileirão')
# print(f'A Chapecoense está na posição {times.count("Chapecoense")}')  # interpolação (observação)
# como o print formatado tem um apóstrofo, se usar outro apóstrofo dá erro, por isso
# tem que usar aspas duplas dentro do print {} que ele interpreta corretamente
