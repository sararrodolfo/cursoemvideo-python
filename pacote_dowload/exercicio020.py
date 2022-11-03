# Desafio 20
# ordem de apresentação dos trabalhos dos alunos
# agora vai aparecer a ordem dos 4
# então são quatro vezes o random e mostrando os nomes

from random import shuffle
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de aparesentação do trabalho será: {lista}')
