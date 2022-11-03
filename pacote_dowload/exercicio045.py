"""DESAFIO 45 - JOGO
pedra
papel
tesoura
as condições do jogo quando ganha:
1. o papel ganha da pedra porque a embrulha
2. a tesoura ganha do papel porque a corta
3. e a pedra ganha da tesoura porque a quebra
assim:
usuário escolhe
o computado escolhe
mais ou menos como aquele jogo
Crie um prgrama que faça o computador jogar Jokenpô com você
"""
# IMPORTANDO MÓDULOS
from time import sleep
from random import choice

# TÍTULO
print('--=--' * 15)
print('VAMOS JOGAR JOKENPÔ...')
print('--=--' * 15)

# ENTRADA
# ESCOLHA DO USUÁRIO
numero = int(input('Você tem as seguintes opções: \n'
                   '1 = papel \n'
                   '2 = tesoura \n'
                   '3 = pedra \n'
                   'Digite sua opção: '))

# OPÇÕES
lista = [1, 2, 3]

# RESPOSTA DO PROGRAMA
resposta = choice(lista)

# PARECE QUE ESTÁ PENSANDO
# frescurinha
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-==-' * 12)

# CONDIÇÃO DE TESTE
if resposta == 1 and numero == 3:
    print('Eu escolhi papel e você escolheu pedra.')
    print('Você PERDEU! O papel embrulha a pedra! \n'
          'Tente de novo!')
elif numero == 1 and resposta == 3:
    print('Você escolheu papel e eu escolhi a pedra.')
    print('VOCÊ GANHOU! O papel embrulha a pedra! \n'
          'Vamos jogar de novo?')
elif resposta == 2 and numero == 1:
    print('Eu escolhi a tesoura e você escolheu o papel.')
    print('Você PERDEU! A tesoura corta o papel! \n'
          'Tente de novo!')
elif numero == 2 and resposta == 1:
    print('Você escolheu a tesoura e eu escolhi o papel.')
    print('Você GANHOU! A tesoura corta o papel! \n'
          'Vamos jogar de novo?')
elif resposta == 3 and numero == 2:
    print('Eu escolhi a pedra e você escolheu a tesoura.')
    print('Você PERDEU! A pedra quebra a tesoura! \n'
          'Tente de novo!')
elif numero == 3 and resposta == 2:
    print('Você escolheu a pedra e eu escolhi a tesoura.')
    print('Você GANHOU! A pedra quebra a tesoura! \n'
          'Vamos jogar de novo?')
else:
    print('Xi, eu escolhi o mesmo que você. E agora? \n'
          'Deu empate! Vamos tentar de novo...')
