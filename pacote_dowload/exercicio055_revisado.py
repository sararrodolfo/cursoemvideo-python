maior = menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c + 1}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior:.0f}kg')
print(f'O menor peso foi {menor:.0f}kg')