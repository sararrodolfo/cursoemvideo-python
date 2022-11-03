# Desafio 010
# leia um valor na carteira
# quantos dólares ele pode comprar
# US$ 1.00 - R$ 3.27
# outras moedas

real = float(input('Digite quanto tem em carteira: R$ '))
dolar_US = real / 4.70205
dolar_canadense = real / 3.70
won = real / 0.0038
iene = real / 0.036
euro = real / 5.02
libra = real / 6.05
print(f'Dá para comprar {dolar_US:.2f} dólares americanos')
print(f'Dá para comprar {dolar_canadense:.2f} dólares canadenses')
print(f'Dá para comprar {won:.2f} wons')
print(f'Dá para comprar {iene:.2f} ienes')
print(f'Dá para comprar {euro:.2f} euros')
print(f'Dá para comprar {libra:.2f} libras')