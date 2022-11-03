"""Aprimorar, colocar se o usuário quer mais números"""

cont = "zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", \
          "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis",\
          "dezessete", "dezoito", "dezenove", "vinte"

while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}')
    else:
        print('Tente novamente.', end='')
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao not in 'SN':
        print('Opção inválida. Tente novamente. Deseja continuar? [S/N] ')
    if opcao == 'S':
        continue
    else:
        print('Programa finalizado. Volte sempre.')
        break
