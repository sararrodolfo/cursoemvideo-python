"""Faça um programa que leia o nome de uma pessoa e
mostre uma mensagem de boas-vindas"""

# Usando o exercício para aplicação de cores
# TÍTULO
print('\33[45m_==-\33[m' * 13)
mensagem = 'PROGRAMA DE BOAS-VINDAS!'
print(f'\33[43m{mensagem: ^52}\33[m')
print('\33[45m_==-\33[m' * 13)

# INFORMAÇÃO DO USUÁRIO
texto = 'Digite seu nome: '
nome = input(f'\33[30;43m{texto}\33[m \n')

# MENSAGEM DE BOAS-VINDAS
print(f'\33[30;43mPrazer em conhecê-lo(a),\33[m \33[1m{nome}\33[m\n'
      f'\33[1;30;43mSeja bem-vindo(a) ao Curso em Vídeo!\33[m\n'
      f'\33[30;43mEstamos no\33[m \33[1mMundo Um: Fundamentos\33[m.\n'
      f'\33[30;43mE para praticarmos, temos que resolver\33[m\n'
      f'\33[1;30;43mTODOS OS EXERCÍCIOS.\33[m\n'
      f'\33[30;43mVai ser uma grande jornada.\33[m\n'
      f'\33[30;43mLembre-se o que o Guanabara diz:\33[m\n'
      f'\33[3;97;43mEu não sei o segredo para o sucesso,\33[m\n'
      f'\33[3;97;43m...Mas para o fracasso, eu sei: é não praticar!!\33[m')
      f'\33[3;97;43m...ENTÃO BORA PRATICAR!!\33[m')

