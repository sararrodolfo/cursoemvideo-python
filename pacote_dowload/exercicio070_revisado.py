"""Qual é o total gasto na compra
Quantos produtos custam mais de 1000
qual é o nome do produto mais barato"""

print('-==' * 20)
print(f'{"LOJA SUPER BARATÃO":^50}')
print('-==' * 20)
soma = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço R$: '))
    if cont == 0:
        barato = produto
        menor = preco
    else:
        if preco < menor:
            preco = menor
            produto = barato
    soma = soma + preco
    cont += 1
    if preco > 1000:
        totmil += 1
    menu = ' '
    while menu not in 'SN':
        menu = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print('-==' * 20)
    if menu == 'N':
        break
print('-==' * 20)
print(f'O total da compra foi R$ {soma:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
