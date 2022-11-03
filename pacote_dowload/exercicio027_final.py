"""Desafio 027
leia o nome completo de uma pessoa mostrando o primeiro e o último nome separadamente
Exemplo: Ana Maria de Souza, primeiro: Ana, último: Souza
que funcione em qualquer tamanho de string"""

nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'Muito prazer  em te conhecer {n[0]}!')  # trocar pelo primeiro nome
print(f'Seu primeiro nome é: {n[0]}')
print(f'Seu último nome é: {n[len(n)-1]}')
