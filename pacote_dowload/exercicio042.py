"""DESAFIO 042 DESAFIO 35 - REFAÇA / triângulo
acrescentando o recurso de mostrar que tipo de triângulo será formado:
- equilátero: todos os lados iguais
- isóceles: dois lados iguais
- escaleno: todos os lados diferentes
--- prestar atenção!! a resposta tem bastante ensinamento
"""
# ENTRADA
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

# CONDIÇÃO
# PRIMEIRA CONDIÇÃO: SE É UM TRIÂNGULO
# todas as condições têm que serem verdadeiras para se formar o triangulo

# SIMPLIFICANDO

# if (b - c) < a < b + c:
#     if (b - c) < b < a + c:
#         if (a - b) < c < a + b:
#             print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO, sendo:')
#         else:
#             print('Não pode')

# REFAZERNDO O EXERCÍCIO
if (b - c) < a < b + c:
    if (b - c) < b < a + c:
        if (a - b) < c < a + b:
            print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO, sendo:')
            equilatero = (a == b) and (b == c)
            isoceles = (a == b) and (b != c)
            escaleno = (a != b) and (b != c)
            if equilatero:
                print('Triângulo equilátero')
            elif isoceles:
                print('Triângulo isóceles')
            elif escaleno:
                print('Triânbulo escaleno')
