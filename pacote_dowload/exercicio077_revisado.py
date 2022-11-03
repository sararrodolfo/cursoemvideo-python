palavras = 'aprender', 'programar', 'linguagem', 'python',\
    'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', \
    'programador', 'futuro'
for p in palavras:
    print('\nNa palavra', end=' ')
    print(f'{p.upper()}, temos as letras: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')
