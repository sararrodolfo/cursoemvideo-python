# Desafio 025
# leia o nome de uma pessoa
# diga se ela tem "Silva" no nome (em qualquer lugar)
# True ou False

nome = str(input('Digite seu nome: ')).strip()
nome_u = nome.upper()
silva = 'SILVA' in nome_u  # processo de encontrar silva independente de como o usuario digita
print(f'O seu nome contém "Silva"? True or False. True (Sim) / False (Não) '
      f'Resposta: {silva}')
