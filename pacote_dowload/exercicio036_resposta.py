casa = float(input('Valor da casa: R$'))
salario = float(input('Valor do salário: R$ '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 /100
print(f'Para pagar uma casa no valor de R$ {casa} em {anos}')
print(f'a prestação será de R$ {prestacao}.')
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO.')
else:
    print('Empréstimo NEGADO!')

# TIVE O MESMO RACIOCÍNIO, PORÉM, AO INVÉS DE SER MÍNIMO PARA SER CONCEDIDO
# USEI O VALOR DA PARCELA ATÉ 30% OU SUPERIOR A 30% COMO CONDIÇÃO PARA SER NEGADO