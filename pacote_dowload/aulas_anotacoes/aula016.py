lanche = ('hamburguer', 'pizza', 'suco', 'pudim', 'batata frita')

# pessoa = 'Gustavo', 39, 'M', 99.88  # pode ter dados de tipos diferentes
# del(pessoa)  # apaga da memória, por isso gera erro na hora de mandar o print posteriormente
#  NameError: name 'pessoa' is not defined
# del(pessoa[1])
# TypeError: 'tuple' object doesn't support item deletion
# print(pessoa)

# a = 2, 5, 4
# b = 5, 8, 1, 2
# c = b + a  # fica com todos os elementos das tuplas, respeitando a ordem do b primeiro e depois o a
# print(len(c))  # aparece a quantidade de elementos do 'c'
# print(c.count(5))  # aparece o resultado de quantas vezes aquele elemento aparece na tupla 'c'
# print(c)
# print(c.index(2))  # como tem duas ocorrências, ele pega somente a primeira

# tuplas são imutáveis, exceto para DELETAR A TUPLA INTEIRA, NÃO DÁ PARA DELETAR ITENS!
# lanche[1] = 'refrigerante'
# TypeError: 'tuple' object does not support item assignment

# print(lanche[-2:])
# se eu quiser fazer diferente usando cada uma das comidas:

# # esse print eu uso minha variável composta
for comida in lanche:
    print(f'Eu vou comer {comida}...')
print('Comi pra caramba!')

# se eu quiser usar o LEN e usar o range:
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]}... na posição {cont}')
# print('Comi pra caramba!')

# eu posso ter o mesmo resultado usando ENUMERATE
# a variável pos é criada e recebe os valores apresentados pelo enumerate
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida}... na posição {pos}')
# print('Comi pra caramba!')

# uma outra forma é usando o SORTED = COLOCAR EM ORDEM ALFABÉTICA, NUMÉRICA, EM 'ORDEM'
# observa que no print é possível verificar que o sorted coloca em colchetes, ele teve que fazer lista
# sorted não altera a tupla, só coloca em ordem
# print(sorted(lanche))
