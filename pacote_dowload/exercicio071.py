valor = int(input('Qual o valor a ser sacado? R$ '))
total = valor
cedula = 50
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédula(s) de R$ {cedula:.2f}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0  # o total de cédula sempre tem que voltar a zero, porque esgotou a qtdade e vai para outra
        if total == 0:
            break


