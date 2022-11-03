"""DESAFIO 063
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os n primeiros elementos de uma
sequência de Fibonacci
Exemplo: 0, 1, 1, 2, 3, 5, 8
Digite um número: 7
os sete primeiros elementos
Erro comum: não é isso, é aprender o que é sequência de fibonacci"""
print('==-==' * 10)
print('Sequência de Fibonacci')
print('==-==' * 10)
n = int(input('Quantos termos você quer? '))
t1 = 0
t2 = 1    # esses valores, 0 e 1 sempre são iguais
print(f'{t1} -> {t2} ', end='')
cont = 3    # porque já inicia com dois termos, logo começa do terceiro termo em diante
while cont <= n:
    t3 = t1 + t2
    print(f'-> {t3} ', end='')
    t1 = t2   # essa transição de valores a medida que vai fazendo os laços
    t2 = t3  # quando volta o laço o t3 já tem outro valor
    cont += 1
print('-> Fim')
