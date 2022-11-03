valores = int(input('Digite um número: ')), \
          int(input('Digite outro número: ')), \
          int(input('Digite o mais um número: ')), \
          int(input('Digite o último número: '))
print(f'Você digitou os valores: {valores}')
if 9 in valores:
    print(f'O valor 9 apareceu {valores.count(9)} vezes')
else:
    print(f'O valor 9 não apareceu nenhuma vez.')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)}a. posição.')
else:
    print(f'O valor 3 não foi ditado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
