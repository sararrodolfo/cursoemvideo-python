"""Desafio 024
Digite o nome de uma cidade e diga se ela começa com o nome "Santo\""""

cidade = str(input('Em que cidade você nasceu?  ')).strip()  # para retirar espaços
print('Analisando o nome da sua cidade...')

# erro de interpretação do enunciado por minha parte (começa com)
# refazendo o enunciado porque eu usei find, sendo que find procura em toda string
# print(cidade[:5] == 'Santo')  ## atenção para os colchetes por se tratar de lista

# upper p/ fazer o teste mesmo que esteja em maius/minus
analise = cidade[:5].upper() == 'SANTO'   # observação para o nome que agora também está SANTO (maiuscula)

print(f'A sua cidade tendo a palavra ** Santo ** retorna Verdadeiro / True,  \n' 
      f'sendo Falso / False caso não a tenha. Assim, a cidade tem ou não a palavra mencionada? \n'
      f'Resposta: {analise}')
