valor = float(input('Valor do empréstimo: R$ '))
salario = float(input('Salário: R$ '))
prazo = int(input('Anos de financiamento: '))
parcela = valor / (prazo * 12)
print(f'O valor da parcela é de R$ {parcela:.2f}')
print('Empréstimo negado' if parcela >= (salario * 0.30) else 'Empréstimo aprovado')
