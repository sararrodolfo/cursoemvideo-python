"""DESAFIO 062
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que quer
mostrar 0 (zero) termos."""

print('Gerador de PA')
print('==-==' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0   # variável para controlar o laço
mais = 10  # 10 é o início de vezes e quanto mais
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais? '))
print(f'Foi apresentado {cont - 1} termos no total.')
print('FIM')
