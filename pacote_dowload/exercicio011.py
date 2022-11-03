# Desafio 011
# leia a largura e a altura de uma parede em metros
# calcule sua área
# quantidade de tinta, sendo: 1 L para 2m2
# largura = float(input('Digite a largura: '))
# altura = float(input('Digite a altura: '))
# area = largura * altura
# quantidade_tinta = area / 2
# print(f'Serão necessários {quantidade_tinta:6.1f} para pintar a parede')

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura * altura
quantidade_tinta = area / 2
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m2')
# print(f'Para pintar essa parede, você precisará de {quantidade_tinta:.0f}l de tinta')
print(f'Para pintar essa parede, você precisará de {quantidade_tinta}l de tinta')