from datetime import date
atual = date.today().year
totmaior = totmenor = 0
for c in range(0, 7):
    ano = int(input(f'Digite o {c + 1} ano de nascimento: '))
    if (atual - ano) > 21:
        totmaior += 1
    if (atual - ano) <= 21:
        totmenor += 1
print(f'No total foram {totmaior} pessoas maiores de idade.')
print(f'No total de {totmenor} pessoas menores de idade.')