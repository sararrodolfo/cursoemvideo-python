"""Desafio 033
Leia 3 números e diga qual é o maior e qual é o menor
3, 7, 5 - por exemplo"""

# Resposta direta - tentei e deu errado porque estou cansada (12:28)
# + de 12 h estudando
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
# verificar qual é o menor e retorna o valor
# a simplicidade é determinar o valor 'a' logo como menor e depois
# fazer o mesmo com o valor maior
menor = a
if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c
# print(f'O menor valor foi {menor}')
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
