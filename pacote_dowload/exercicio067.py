"""Tabuada"""
print('==-==' * 10)
print(("==-==" * 4), 'TABUADA ', ("==-==" * 4))
print('==-==' * 10)
while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    cont = 0
    if tabuada < 0:
        break
    while cont <= 10:
        print(f'{tabuada} x {cont} = {tabuada * cont}')
        cont += 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')