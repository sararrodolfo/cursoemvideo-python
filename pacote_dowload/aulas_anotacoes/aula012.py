"""ESTRUTURAS CONDICIONAIS ANINHADAS"""

# ESTRUTURA CONDICIONAL COMPOSTA
nome = str(input('Qual é o seu nome? '))
print(f'Tenha um bom dia, {nome}')
if nome == 'Gustavo':
    print('Que nome bonito!')

# COLOCANDO ELIF - TORNA-SE UMA ESTRUTURA CONDICIONAL ANINHADA
# POSSO USAR QUANTAS VEZES EU QUISER O ELIF
# UMA COISA DENTRO DA OUTRA
elif nome == 'Pedro' or nome == 'Maria' or nome  == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana, Cláudia, Jéssica, Juliana':  # dentro desses exemplos
    print('Belo nome feminino!')

# SEM O ELSE NÃO APRESENTA ESSA MENSAGEM, PORÉM, É OPCIONAL
else:
    print('Seu nome é bem comum...')