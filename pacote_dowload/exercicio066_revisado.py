cont = soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    # cont += 1  # se colocar o cont aqui, o flag será contado
    if n == 999:
        break
    cont += 1  # portanto, o contador deve estar depois da condição de parada acima
    # ou seja, quando o número digitado for 999, imediatamente, ele cessa,
    # sem fazer a soma do número digitado
    soma += n
print(f'Foram digitados {cont} e a soma dos valores foi {soma}.')
