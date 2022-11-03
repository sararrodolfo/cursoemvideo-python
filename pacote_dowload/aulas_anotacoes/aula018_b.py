galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  # [[], [], []] (lista vazia se eu coloco apenas galera.append(dados)
    dado.clear()
# print(galera)  # [['Pedro', 22], ['Maria', 33], ['Cláudia', 55]]
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade')
