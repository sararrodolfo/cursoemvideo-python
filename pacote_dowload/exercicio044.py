"""DESAFIO 44 - PRODUTO
Elabore um programa que calcula o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- a vista - dinheiro/cheque: 10% de desconto
- a vista - cartão: 5% de desconto
- em até 2 vezes no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
# ENTRADA
# VALOR DO PRODUTO
valor = float(input('Digite o valor do produto: R$ '))

# FORMA DE PAGAMENTO
pagamento = int(input('Qual será a forma de pagamento? \n'
                      'Digite abaixo: \n'
                      'Opção ZERO (0) - à vista em dinheiro ou cheque \n'
                      'Opção UM (1) - à vista no cartão \n'
                      'Opção DOIS (2) - parcelado em duas vezes no cartão \n'
                      'Opção TRÊS (3) - parcelado em três vezes no cartão \n'
                      'Digite a opção desejada:   '))
if pagamento == 0:
    print(f'O valor para pagamento com 10% de desconto é de R$ {valor * 0.9:.2f}')
elif pagamento == 1:
    print(f'O valor para pagamento com 5% de desconto é de R$ {valor * 0.95:.2f}')
elif pagamento == 3:
    print(f'O valor para pagamento parcelado em 3x com juros de 20%  é de R$ {valor * 1.20:.2f}')
else:
    print(f'O valor para pagamento parcelado em duas vezes é de R$ {valor}')

