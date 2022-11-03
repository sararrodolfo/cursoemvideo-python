"""Desafio 089
crie um programa que leia nome e duas notas de vários alunos
e guarde tudo numa lista composta
No final, mostre um boletim contendo a média de cada aluno e
permita que o usuário possa mostrar as notas de cada aluno
individualmente
3 níveis de lista
faz uma listona com o nome
dentro da listona eu tenho uma lista menor
dentro da listinha menor eu tenho outra listinha menor
guarda a média também
faz uma tabela com código, nome, média dos alunos
Mostrar a média de qual aluno? 999 para interromper
Finalizando - sleep de novo
<<< Volte sempre >>>
"""
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(30 * '-=')
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print(30 * '-=')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')