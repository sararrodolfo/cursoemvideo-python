# ANALISADOR DE TRIÂNGULO

print('-==-' * 13)
titulo = 'ANALISADOR DE TRIÂNGULO'
print(f'{titulo: ^50}')
print('-==-' * 13)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
# todas as condições têm que serem verdadeiras para se formar o triangulo
if (b - c) < a < b + c:
    if (b - c) < b < a + c:
        if (a - b) < c < a + b:
            print('Os segmentos acima PODEM FORMAR triângulo.')
        else:
            print('Não pode')
