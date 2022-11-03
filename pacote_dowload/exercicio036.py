"""Desafio 36 - EMPRESTIMO BANCÁRIO
Escreva um programa para aprovar empréstimo bancário para a compra de uma casa
O programa vai perguntar:
- o valor da casa
- o salário do comprador
- e quantos anos ele vai pagar
Ex: 200 mil, 1 mil reais, 50 anos (não vai correr juros)
O valor da parcela não pode exceder 30%
Calcule o valor da prestação mensal
sabendo que ele não pode exceder 30% do salário
ou então
o empréstimo será negado"""

# IMPORTAÇÃO
from time import sleep

# TÍTULO COM CORES
print('\33[1;30;107m-==-\33[m' * 13)
titulo = 'SIMULADOR DE EMPRÉSTIMO BANCÁRIO: realize seus sonhos!'
print(f'\33[1;32;107m{titulo: ^52}\33[m')
print('\33[1;30;107m-==-\33[m' * 13)

# CONTRUÇÃO DO PROGRAMA
# DEFININDO O VALOR DA CASA
valor_casa = float(input('\33[3;30;107mDigite o valor do imóvel: R$  \33[m'))

# DEFININDO O VALOR DO SALÁRIO
salario = float(input('\33[3;30;107mDigite o valor do salário bruto/mensal: R$  \33[m'))

# DEFININDO PRAZO DESEJADO DE PAGAMENTO
prazo = int(input('\33[3;30;107mDigite quantos anos deseja realizar o pagamento? \33[m'))

# BRINCADEIRINHA
print('\33[1;32;107mANALISANDO A SOLICITAÇÃO...\33[m')
sleep(2)

print(f'\33[1;30;107mDe acordo com as informações prestadas:\33[m \n'
      f'\33[3;30;107m- Valor da imóvel: R$ {valor_casa:.2f}\33[m \n'
      f'\33[3;30;107m- Salário mensal (bruto): $R$ {salario:.2f}\33[m \n'
      f'\33[3;30;107m- Prazo de pagamento: {prazo} anos.\33[m \n'
      f'\33[1;30;107mTem se que:\33[m')

# CÁLCULOS E CONDIÇÕES
# CONDIÇÕES - IF, ELIF, ELSE
# TRANSFORMANDO ANOS EM MESES
meses_prazo = prazo * 12
# OBTENDO O VALOR DA PARCELA
valor_parcela = valor_casa / meses_prazo
# PRA SIMPLIFICAR A CONDIÇÃO
# limite_parcela = salario * 0.30
# limite_parcela = salario * (30 / 100)

# CONDIÇÃO: [ÚNICA] NÃO PODE ULTRAPASSAR 30% DO SALÁRIO, LOGO:
if valor_parcela >= salario * 0.30:
    print(f'\33[1;31;107mValor da parcela: R$ {valor_parcela:.2f} \33[m\n'
          '\33[1;31;107mEMPRÉSTIMO NEGADO: \33[m\n'
          '\33[1;31;107mInfelizmente, o valor da parcela excede em mais de 30% do seu salário.\33[m \n')
else:
    print(f'\33[1;32;107mValor da parcela: R$ {valor_parcela:.2f} \33[m\n'
          '\33[1;32;107mEMPRÉSTIMO PODE SER CONCEDIDO!\33[m\n'
          '\33[1;32;107mPARABÉNS!\33[m\n'
          '\33[1;32;107mRealize seu sonho!\33[m')
