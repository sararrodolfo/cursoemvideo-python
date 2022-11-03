"""Desafio 027
leia o nome completo de uma pessoa mostrando o primeiro e o último nome separadamente
Exemplo: Ana Maria de Souza, primeiro: Ana, último: Souza
que funcione em qualquer tamanho de string"""

# nome = input('Digite seu primeiro nome: ')
# meio = input('Digite seu nome do meio: ')
# ultimo = input('Digite seu sobrenome: ')
#
# print(f'O seu primeiro nome é {nome}, sendo o seu sobrenome {ultimo}')

# alternativa 2
nome1 = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
nome1_dividido = nome1.split()
# print(nome1_dividido)
print(f'O seu primeiro nome é: {nome1_dividido[0]}')  # lista: 0, retorna o primeiro
print(f'O seu último nome é: {nome1_dividido[-1]}')  # lista: -1, retorna o último
