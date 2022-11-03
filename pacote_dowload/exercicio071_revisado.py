print("====" * 15)
print(f'{"BANCO CEV":^55}')
print("====" * 15)
valor = int(input('Qual valor você quer sacar? R$ '))
# primeiro ponto não tem contador!
total = valor  # o montante a ser sacado
ced = 50
totalced = 0  # a quantidade de cédulas que serão entregues
while True:   # um loop infinito que só será falso quando o total for zerado
    if total >= ced:  # se o total for maior ou igual a cédula
        total -= ced  # subtrai do total o valor da cédula
        totalced += 1  # começa a contagem das cédulas
        # quando se tornar falsa a expressão total maior ou igual à cédula
    else:
        if totalced > 0:  # se o total de cédulas foi maior que zero ou nenhuma cédula
            print(f'Total de {totalced} cédulas de R$ {ced:.2f}')  # imprime
        # nova condição já que a cédula anterior era maior que o total
        if ced == 50:
            ced = 20
        # se a cédula for menor que o total, retoma a condição verdadeira de cima
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0  # precisa zerar o total de cédulas, porque já foi impressa a quantidade
        # de cédulas quando retornou a condição falsa
        if total == 0:  # nesse ponto, já se verificou todas as cédulas
            break   # interrompe o loop
print('Obrigado por usar o Banco do Curso em Vídeo. Volte sempre!')

