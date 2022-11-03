"""imagina que eu faço um print de 'oi' - 6 vezes, mas imagina que seriam 10000 vezes. Complicado"""

# ESTRUTURA DE REPETIÇÃO - USO DO FOR IN RANGE

# for c in range (1, 6):
#     print('Oi')
# print('FIM')

"""por que ele escreveu 5 vezes e não 6? - de 1 até 5, no 6 ele para, ele não considera o último
de zero a 6 - aí ele considera
"""
# for c in range (0, 6):
#     print('Oi')
# print('FIM')

# for c in range (0, 6):
#     print('Oi')
#     print('FIM')
""" eu coloquei uma tabulação a mais, olha como ele se comporta agora: Oi, FIM, Oi, FIM
 O COMANDO FIM ESTÁ DENTRO DO COMANDO FOR, CUIDADO COM ESSA IDENTAÇÃO
"""
# for c in range (0, 6):
#     print(c)
# print('FIM')
# se eu colocar o 'c' - que nem definido está, ele imprime de 0 até 5, seguido do FIM

"""# preciso de uma contagem de 1 até 6"""
# for c in range (1, 7):
#     print(c)
# print('FIM')

"""contagem de 6 até - ZERO, o que seria para trás, na regressiva, tem que colocar o - 1:
- 1 - qual é a iteração
o que é que vai acontecer no final do laço (vai tirar um de cada um dos elementos)  """
# for c in range (6, 0, -1):  # não apareceu o zero
#     print(c)
# print('FIM')

""" se eu colocar 0, 7, 6 - ele coloca múltiplos de 2
ele contou de zero até sete 
pulando de dois em dois
faça vários testes """

# for c in range (0, 7, 2):  # não apareceu o zero
#     print(c)
# print('FIM')

"""exemplo de contador, novamente, dessa forma, com o input"
- saída: não vem o número 7
para incluir o 7 tem que ser n+1"""

# n = int(input('Digite um valor: '))
# for c in range(0, n):
#     print(c)
# print('Fim')

""" eu consigo ler um valor, aqui em 'n' - do input
e utilizar esse 'n'
como parte de passagem para o 'for'
posso usar essa mesma linha de raciocínio de várias maneiras """
# n = int(input('Digite um valor: '))
# for c in range(0, n+1):
#     print(c)
# print('Fim')

"""
3 valores
incío
fim e
passo
Resposta: entendi que começa a contagem a partir do 2 vai até 9+1 e de 3 em três
Saída: 2, 5, 8, Fim
Exemplo 2: Início 1, Fim 100, Passo 10
Saída: 1, 11, 21, 31 ... 91, Fim
"""
# i = int(input('Inicio: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# for c in range(i, f+1, p):
#     print(c)
# print('Fim')

"""Imagina que eu tenho que pedir 10 vezes o valor ao usuário
cria o laço para que seja repetido (0 ,10)
define a variável de repetição - n
esaída: digite um valor: 10 vezes
"""
# for c in range(0, 10):
#     n = int(input('Digite um valor:'))
# print('Fim')

'''
eu quero ter o somatório desses números
eu crio o laço
defino 's' recebendo zero
e faço a soma no laço
*** s = s + n *** - observa que s = s fica s+= para não ficar repetindo
ou como podemos uar no Python
s += n
'''
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores é {s}')