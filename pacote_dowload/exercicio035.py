"""Desafio 035
Desenvolva um programa que leia o comprimento de tres retas e
diga ao usuário se elas podem ou não formar um triângulo
r1 r2 r3
existe um princípio matemático que prevê quando dá e
quando não dá para formar um triângulo

CONDIÇÃO

Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
um de seus lados deve ser maior que o valor absoluto (módulo)
da diferença dos outros dois lados e
menor que a soma dos outros dois lados. Veja o resumo da regra abaixo:
(B - C) < A < B + C
(A - C) < B < A + C
(A - B) < C < A + B

Exemplo:
Com os três segmentos de reta medindo 5cm, 10cm e 9cm, podemos formar um triângulo?
Vamos aplicar a regra da condição de existência de um triângulo para todos os lados.
|10 – 9| < 5 < 10 + 9
1 < 5 <19 (VERDADEIRO)

|9 – 5| < 10 < 9 + 5
4 < 10 < 14 (VERDADEIRO)

|5 – 10| < 9 < 10 + 5
5 < 9 < 15 (VERDADEIRO)

Quando um lado não obedece à regra não é possível existir um triângulo."""

# MINHA RESPOSTA

a = int(input('Digite o valor '))
b = int(input('Digite '))
c = int(input('Digite '))
# todas as condições têm que serem verdadeiras para se formar o triangulo
if (b - c) < a < b + c:
    if (b - c) < b < a + c:
        if (a - b) < c < a + b:
            print('Pode ser triangulo')
        else:
            print('Não pode')
