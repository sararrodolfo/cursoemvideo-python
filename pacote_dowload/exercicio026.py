"""Desafio 026
leia a frase do teclado
quantas vezes aparece a letra a
em que posição ela aparece a primeira vez
em que posição ela aparece a última vez"""

# código-fonte
frase = str(input('Digite uma frase qualquer: ')).strip()

# primeiro tem que colocar tudo em lower
frase_c = frase.lower().count('a')
print(f'A quantidade de vezes que aparece que A aparece na frase: {frase_c}')

# mostrar a posição da 1º letra a encontrada
mostrar_posicao = frase.lower().find('a') + 1   # para não ficar esquisito retornar Zero (+1)
print(f'A primeira vez que ela aparece é na posição: {mostrar_posicao}')

# mostrar a última vez que ela aparece
ultima = frase.rfind('a') + 1   # para aparecer a posição mais agradável
print(f'A última vez que ela aparece é na posição: {ultima}')
