"""
É muito importante que a variável cont seja incrementada para evitar
que o loop seja infinito
"""

cont = 0
while cont <= 10:
    print(cont, '* 5 = ', (cont * 5))
    cont += 1
else:
    print('Tabuada do 5 calculada com sucesso!')
