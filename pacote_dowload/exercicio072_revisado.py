extenso = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', \
          'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', \
    'dezessete', 'dezoito', 'dezenove', 'vinte'
n = int(input('Digite um número entre 0 a 20: '))
if not 0 < n < 20:
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[n]}.')
