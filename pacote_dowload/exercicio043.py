"""DESAFIO 43 - IMC
É calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).
imc = peso / altura ** 2
Desenvolva uma lógica que leia o peso e a altura de uma pessoa
calcule o imc
e mostre o status de acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.0 e 25: peso ideal
- entre 25 até 30: sobrepeso
- entre 30 e 40: obesidade
- acima de 40: obesidade mórbida
"""
# DADOS DE ENTRADA
nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso(kg): '))
altura = float(input('Digite sua altura(m): '))

# CÁLCULO
imc = peso / altura ** 2
print(f'Seu IMC de {imc:.1f} é considerado:')

# CONDIÇÕES
if imc <= 18.5:
    print('abaixo do peso')
elif 18.5 < imc <= 25.0:
    print(' peso ideal')
elif 25 < imc <= 30:
    print('sobrepeso')
elif 30 < imc <= 40:
    print('obesidade')
elif imc > 40:
    print('obesidade mórbida')
