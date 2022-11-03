"""Desafio 007
leia duas notas de um aluno, calcule e mostre a média
"""
# USANDO PARA CORES
# TITULO DO PROGRAMA
print('\33[7;31;40m *(*)(*) (*)(*)* \33[m' * 4)  # inversao cor 31 - vermelho
mensagem = 'OPERAÇÕES MATEMÁTICAS: **  MÉDIA  **'
print(f'\33[1;32;107m{mensagem: ^68}\33[m')
print('\33[7;97;40m *(*)(*) (*)(*)* \33[m' * 4)  # inversao cor 97 - branco

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print(f'A média do aluno entre {n1:.1f} e {n2:.1f} é {media:.1f}')
