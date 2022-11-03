"""Desafio 66
desconsiderar o flag e apresentar a soma dos valores digitados"""
s = cont = 0
while True:
    n = int(input('Digite um número [999] para parar: '))
    if n == 999:
        break
    cont += 1
    s += n

print(f'A soma do(s) {cont} números digitados é {s}.')
