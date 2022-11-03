"""Desafio 046
contagem regressiva com o uso do for: de zero a 10 com 1 segundo de pausa
"""

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(0.1)
print('Booom!')
