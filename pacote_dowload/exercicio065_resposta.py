resp = 'S'
soma = quantidade = media = menor = maior = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar: [s/n] ')).strip().upper()[0]
media = soma / quantidade   # deixa fora do laço para não repetir sem necessidade
print(f'Você digitou {quantidade} números e a media foi {media:.2f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
