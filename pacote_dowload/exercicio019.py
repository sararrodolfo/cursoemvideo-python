"""Desafio 019
sortear quatro alunos para apagar o quadro
ler o nome deles e escrevendo o nome do escolhido
provavelmente usar o random e o número obtido vincular a um aluno

import random
n1 = str(input('Digite o nome do aluno 1: '))
n2 = str(input('Digite o nome do aluno 2: '))
n3 = str(input('Digite o nome do aluno 3: '))
n4 = str(input('Digite o nome do aluno 4: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi: {escolhido}')"""

from random import choice
n1 = str(input('Digite o nome do aluno 1: '))
n2 = str(input('Digite o nome do aluno 2: '))
n3 = str(input('Digite o nome do aluno 3: '))
n4 = str(input('Digite o nome do aluno 4: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O aluno escolhido foi: {escolhido}')
