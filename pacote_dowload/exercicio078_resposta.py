listanum = []
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('-==' * 30)
print(f'Você digitou os números: {listanum}')
print(f'O maior valor digitado foi {maior}, na(s) posição(ões) ', end='')
# eu vou ter que varrer a minha lista
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
    if v == menor:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} na(s) posição(ões) ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
