# # Desafio 013
# # Leia o salário de 1 funcionário
# # mostre seu novo salário com 15% de aumento
# salario_inicial = float(input('Digite seu salário: R$ '))
# salario_aumento = (salario_inicial * 1.15)
# print(f'O seu salário teve aumento de 15%, atualmente sendo: R$ {salario_aumento:8.2f}')
#
# # Exercício alternativo com desconto e aumento em um produto

valor_produto = float(input("Digite o valor do produto? R$ "))
a_vista = valor_produto - (valor_produto * 10 / 100)
parcelado = valor_produto + (valor_produto * 8/100)
print(f'O valor do produto é de R$ {valor_produto:.2f}, sendo \n '
      f'- A vísta (com 10% desconto: R$ {a_vista:.2f}) \n '
      f'- Parcelado (com 8% de acréscimo: R$ {parcelado:.2f})')
