"""Desafio 051
Desenvolva um programa que leia o primeiro termo e a razão de um PA - progressão aritmética .
No final, mostre os 10 primeiros termos dessa progressão.
... é uma contagem que vai pulando de tanto até tanto - de 1 até 100, pulando de 10 em 10, isso é uma PA
onde o primeiro elemento é 1 e o último é 10 (razão)"""

# o que é importante aprender é
# compreender o enunciado e verificar que não usa,
# nem soma, nem cont, mas tem uma variável no intervalo

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' -> ')
print('ACABOU!')
