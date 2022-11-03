# ENTRADA
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

# REFAZERNDO O EXERCÍCIO
# COLOCA TODAS AS CONDIÇÕES NUMA LINHA SÓ
if (b - c) < a < b + c and (b - c) < b < a + c and (a - b) < c < a + b:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO, sendo:', end=" ")
# CONDIÇÃO PARA VERIFICAR O TIPO
    if a == b == c:
        print('EQUILÁTERO!')
    if a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Não podem formar um triângulo.')
