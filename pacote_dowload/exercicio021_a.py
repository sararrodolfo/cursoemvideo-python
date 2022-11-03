# Desafio 21
# Faça um programa em Python que abra e reproduza um arquivo em MP3
# Emocionante! <3 Duas coisas que eu amo: música e - agora - aprender Python!
import emoji
print(emoji.emojize(':red_heart: Eu amo essa música :red_heart:', language='alias'))
print('Foi a primeira música coreana que eu me apaixonei. \n'
       'Cantor: Jannabi \n'
       'Música: A story I could not see \n'
       'Trilha Sonora de: Romance is a Bonus Book, Netflix')
from playsound import playsound
playsound(r'ex21.mp3')
