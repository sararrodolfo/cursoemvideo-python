"""DESAFIO 44 - PRODUTO
Elabore um programa que calcula o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- a vista - dinheiro/cheque: 10% de desconto
- a vista - cartão: 5% de desconto
- em até 2 vezes no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""


print(f'{"### LOJAS GUANABARA":=^40}')
# ENTRADA
# VALOR DO PRODUTO
valor = float(input('Preço das compras: R$ '))

# FORMA DE PAGAMENTO
pagamento = int(input('''FORMA DE PAGAMENTO 
                      'Digite abaixo:
                      '[ 0 ]- à vista / dinheiro ou cheque 
                      '[ 1 ] - à vista / cartão 
                      '[ 2 ] - parcelado em 2x vezes no cartão 
                      '[ 3 ] - parcelado em 3x ou + no cartão 
                      'Digite a opção desejada:   '''))
if pagamento == 0:
    print(f'O valor da sua compra foi de R$ {valor:.2f}')
    print(f'O valor de desconto é de R$ {valor * 0.1:.2f}')
    print(f'O valor para pagamento com 10% de desconto é de R$ {valor * 0.9:.2f}')
elif pagamento == 1:
    print(f'O valor da sua compra foi de R$ {valor:.2f}')
    print(f'O valor de desconto é de R$ {valor * 0.05:.2f}')
    print(f'O valor para pagamento com 5% de desconto é de R$ {valor * 0.95:.2f}')
elif pagamento == 3:
    parcela = int(input('Quantas parcelas? '))
    valor_j = valor * 0.20
    v_parcela = (valor_j + valor) / parcela
    print(f'O valor da sua compra de R$ {valor:.2f}, com juros de 20% , é de R$ {valor_j:.2f} \n'
          f'Valor total de sua compra atualizado com juros é de R$ {valor + valor_j:.2f}, \n'
          f'Valor de parcela: R$ {v_parcela:.2f}')
elif pagamento == 4:
    print(f'O valor da sua compra de R$ {valor:.2f} não tem juros ou desconto.\n'
          f'Valor da parcela: {valor / 2:.2f}')
else:
    print(f'\33[1;31mOPÇÃO INVÁLIDA. Tente novamente. \n'
          f'Sua compra de R$ {valor:.2f} vai custar R$ {valor:.2f} no final. \33[m')
