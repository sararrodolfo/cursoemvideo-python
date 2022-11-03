"""
VARIÁVEIS COMPOSTAS - LISTAS
"""
num = [2, 5, 9, 1]
num[2] = 3  # alterar o valor
# num[4] = 7 # erro no modo de inserção
num.append(7)  # inclui no último elemento
num.sort(reverse=True)  # ordem reversa
# num.insert(2, 0)  # na posição 2, inserir o valor zero
num.insert(2, 2)
# num.remove(2)  # ele remove o primeiro elemento encontrado com o valor a ser eliminado
"""ficando, portanto, a lista 7, 5, 3, 2, 1
esse segundo dois ele não tira!"""
if 4 in num:
    num.remove(4)
else:
    print('Eu não achei o número 4')
# num.pop()  # elimina o último elemento
# num.pop(2)  # ele elimina o segundo elemento
print(num)
print(f'Essa lista tem {len(num)} elementos')  # para verificcar quantos elementos tem
