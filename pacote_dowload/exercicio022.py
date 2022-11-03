# Deafio 022 # nome completo de uma pessoa
# letras maiusculas # letras minúsculas
# quantas letras ao tdo- sem considerar os espaços # quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print(f'O seu nome é: {nome}, em letras maísculas fica assim {nome.upper()}')
print(f'Enquanto o seu nome em minúscula fica assim {nome.lower()}')

# mais simples de entender (esse exercício, segundo o professor)
# nomed = nome.split()
# nome1 = len(nomed[0])
# nome2 = len(nomed[1])
# nome3 = len(nomed[2])
# total_nome = (nome1 + nome2 + nome3)
print(f'A quantidade de letras é: {len(nome) - nome.count(" ")}')

## encontre o primeiro espaço - vai me retornar a quantidade de letras que
# antecedem o nome (0 - A, 1 - N, 3 - A, 4 - " ", sendo que ele lê um anterior, então são 3
primeiro = nome.find(' ')
print(f'Seu primeiro nome tem {primeiro}')
