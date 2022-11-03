"""Desafio 077
quais as vogais estão nas palavras
"""

palavras = 'aprender', 'programar', 'linguagem', 'python',\
    'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', \
    'programador', 'futuro'
cont = 0
for p in palavras:
    print(f'\nNa palavra {palavras[cont].upper()} temos', end=' ')
    cont += 1
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
