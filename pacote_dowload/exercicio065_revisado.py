soma = media = maior = menor = cont = 0
resp = 'S'
while resp == 'S':
    num = int(input('Digite um valor: '))
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma = soma + num
    resp = str(input('Deseja inserir mais valores? [S]im/[N]ão]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = (str(input('Opção inválida. Deseja inserir mais valores? '
                          '[S]im/[N]ão]: '))).strip().upper()[0]
media = soma / cont
print(f'A média dos valores digitados é: {media:.0f}.')
print(f'O maior número é {maior} e o menor número é {menor}.')
