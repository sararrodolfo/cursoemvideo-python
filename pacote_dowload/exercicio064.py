"""DESAFIO 064
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999
que é a condição de parada
No final, mostre quantos numeros foram digitados e qual foi a soma entre eles
(desconsiderando o flag)
- lembra o exercício da aula"""

# num = 0
# soma = 0
# cont = 0
# por essas três variaveis ter o valor zero, pode ser feito assim:
soma = cont = 0   # só para que aprendessemos a questão de ser tudo zero
num = int(input('Digite um número [999] para parar: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999] para parar: '))
print(f'Foram digitados {cont} numeros e a soma deles é {soma}.')

# para prevenir a gambiarra de -999 e -1 no cont