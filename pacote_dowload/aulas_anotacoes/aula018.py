teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])  # [['Maria', 22], ['Maria', 22]] se eu colocar galera.append(teste) sem o fatiamento
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])  # [['Gustavo', 40], ['Maria', 22]] do jeito que está, faz uma cópia devido ao fatiamento
print(galera)  # [['Maria', 22], ['Maria', 22]]
