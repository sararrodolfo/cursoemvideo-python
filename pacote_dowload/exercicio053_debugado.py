frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()  # aqui eu consigo dividr a frase em palavras
junto = ''.join(palavras)  # agora as palavras estão juntas desconsiderando os espaços
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo.')