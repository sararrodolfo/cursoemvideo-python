"""Desafio 053
Crie um programa que leia uma frase qualquer e diga se ela é PALINDROMO, desconsiderando os espaços.
Exemplo: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA
desconsiderar sem acento, espaços"""

# frase = str(input('Digite uma frase: '))  # começando com a frase
# frase = str(input('Digite uma frase: ')).strip()  # tirar os espaços entre as palavras
"""já deixo tudo em maiúscula para não ter problema na comparação"""
frase = str(input('Digite uma frase: ')).strip().upper()
"""eu vou dividir essas palavras, ou seja, vou separar essa frase em uma lista ou coleção"""
palavras = frase.split()
"""eu vou criar uma variável 'tudo junto' - quando dei o split, ele separou pelos espaços
agora eu consigo juntar, com o JOIN"""
junto = ''.join(palavras)
"""agora as palavras estão juntas desconsiderando os espaços entre elas
Então, até agora, já tem:
- o usuário digita uma frase
- eu splito ela - separo numa lista/coleçao
- junto desconsiderando os espaços, ou seja, elimino os espaços
AGORA EU CONSIGO VARRER ESSA STRING DE TRÁS PARA FRENTE
- crio a variável inverso que recebe 'nada', vazia"""

"""
dá para fazer sem nem usar o for
basta usar o fracionamento
inverso = junto[::-1]"""

inverso = ''

# for letra in range - da última até a primeira
"""a última eu consigo pegando o len (do junto), - 1 voltar um passo negativo"""
# for letra in range(len(junto) - 1, - 1, - 1):

for letra in range(len(junto) - 1, -1, -1):
    """não é do 1 ao 20 em 'letra', é do zero ao 19
    antes da primeira letra, -1
    exemplo: print(junto[letra])
    aqui se usa colchete!! entre o contador letra"""
    # print(junto[letra])
    inverso += junto[letra]
    """eu não quero que imprima o inverso, eu quero que seja o inverso + junto da letra"""

# para finalizar: a condição
"""Se inverso for igual ao junto, é palíndromo"""
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO.')
