num = int(input('Digite um valor [999] para parar: '))
cont = soma = 0
while num != 999:
    cont += 1
    soma = soma + num
    num = int(input('Digite um valor [999] para parar: '))
print(f'Foram digitados {cont} números e a soma dos valores digitados é {soma}')
