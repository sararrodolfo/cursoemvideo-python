# Desafio 027
# leia o nome completo de uma pessoa
# mostrando o primeiro e o último nome separadamente
# Exemplo: Ana Maria de Souza, primeiro: Ana, último: Souza
# que funcione em qualquer tamanho de string

nome = str(input('Digite seu nome: ')).strip()
lista_nome = nome.split()
primeiro = (lista_nome[0])
ultimo = (lista_nome[0:])
print(ultimo)
print(f'O seu primeiro nome é {primeiro} e o seu segundo nome é')

