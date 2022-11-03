cont = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor? (< 0 para nenhuma): '))
    print('---' * 20)
    if num < 0:
        print('Programa encerrado. Volte sempre!')
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {(num * c)}')
        cont += 1
    print('---' * 20)

