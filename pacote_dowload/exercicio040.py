"""DESAFIO 40 - MEDIA 2
Crie um programa que leia duas notas de um aluno e
calcule sua média, mostrando uma mensagem no final
de acordo com a média atingida:
- média abaixo de 5.0: reprovado
- média entre 5.0 e 6.9: recuperação
- média entre 7.0 ou superior: aprovado
"""

# ENTRADA
nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2: '))

# CALCULO DA MÉDIA
media = (nota1 + nota2) / 2

# CONDIÇÕES
if media < 5.0:
    print('Reprovado')
elif media >= 5 and media <= 6.9:
    print('Recuperação')
elif media >= 7.0:
    print('Aprovado')
