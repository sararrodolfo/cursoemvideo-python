"""DESAFIO 062
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que quer
mostrar 0 (zero) termos.
quero mais 20 termos
quantos termos você quer?
zero - nenhum
PERSISTA!!"""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (razao - 1) * razao

contador = primeiro - 1

while contador < decimo:
    if contador < primeiro:
        contador += 1

    else:
        contador += razao
    print(f'{contador}', end=' -> ')

print('Acabaram os termos solicitados.')
print('Deseja mais termos?')
print('[1] Sim ou [0] Para nenhum termo')
opcao = int(input('Digite sua opção: '))
if opcao == 0:
    print('Fim')

else:
    while opcao == 1:
        primeiro = int(input('Primeiro termo: '))
        razao = int(input('Razão: '))
        decimo = primeiro + (razao - 1) * razao

        contador = primeiro - 1

        while contador < decimo:
            if contador < primeiro:
                contador += 1

            else:
                contador += 10
            print(f'{contador}', end=' -> ')

        print('Acabaram os termos solicitados.')
        print('Deseja mais termos?')
        print('[1] Sim ou [0] Para nenhum termo')
        saida = int(input('Digite sua opção: '))
        if saida == 0:
            print('Fim')
            break
