print('LOJA SUPERBARATÃO')
soma = maior = menor = 0

while True:
    nome = str(input('Nome do produto: '))

    preco = float(input('Preço: R$ '))

    if preco >= 1000.00:
        maior += 1

    soma = soma + preco

    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if opcao in 'N':
        print(f'O total da compra foi de R$ {soma:.2f}')
        print(f'Temos {maior} produtos custando mais R$ 1.000,000')
        print(f'O produto mais barato foi {nome} que custa {menor}')
        break
