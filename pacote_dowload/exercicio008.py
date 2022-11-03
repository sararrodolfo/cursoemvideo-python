""""Desafio 008 - TRANSFORMANDO CENTÍMETROS EM MILIMETROS
leia um número
converta em centímetros / milímetros
"""""
# USANDO PARA CORES
# TITULO DO PROGRAMA
print('\33[30;40m *(*)(*) (*)(*)* \33[m' * 4)  # inversao cor 31 - vermelho
mensagem = 'OPERAÇÕES MATEMÁTICAS: TRANSFORMANDO NÚMEROS'
print(f'\33[1;30;107m{mensagem: ^68}\33[m')
print('\33[30;40m *(*)(*) (*)(*)* \33[m' * 4)  # inversao cor 97 - branco

# TRANSFORMANDO METROS EM CENTÍMETROS E MILIMETROS
# ENTRADA
num = int(input('\33[1;31;107mDigite a quantidade de metros: \33[m'))

# CÁLCULO
cent = num * 100
mil = num * 1000

# SAÍDA
print(f'\33[1;31;107mO valor em centímetros é {cent:.0f}, em milímetros é {mil:.0f}\33[m')

