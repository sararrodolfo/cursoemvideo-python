# DADOS DE ENTRADA
nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso(kg): '))
altura = float(input('Digite sua altura(m): '))

# CÁLCULO
imc = peso / altura ** 2
print(f'Seu IMC de {imc:.1f} é considerado:')

# CONDIÇÕES
if imc < 18.5:
    print('Você está ABAIXO DO PESO NORMAL!')
elif 18.5 <= imc <= 25.0:
    print('PARABÉNS, você eno seu PESO IDEAL!')
elif 25 <= imc <= 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc <= 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
