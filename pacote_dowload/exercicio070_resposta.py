tot = totmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço R$: '))
    cont += 1
    tot += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'FIM DO PROGRAMA')
print(f'O total da compra foi de R$ {tot:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {barato} e custa R$ {menor:.2f}')
