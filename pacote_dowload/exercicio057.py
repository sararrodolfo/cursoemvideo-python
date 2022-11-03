""" DESAFIO 057
Faça um programa que leia o sexo de uma pessoa, mas só aceite "M" ou "F".
Caso esteja errado, peça a digitação novamente até ter um valor correto."""

sexo = str(input('Digite seu sexo. [M]asculino ou [F]eminino: ')).strip().upper()
if sexo.isnumeric():   # se o usuário digitar número
    print('Opção inválida. Somente letras: M ou F')

while sexo != 'F' and sexo != 'M':
    print('Digite novamente')
    novamente = str(input('Apenas as opções: [M]asculino ou [F]eminino: ')).strip().upper()
    sexo = novamente
print('Você declarou corretamente seu sexo.')

