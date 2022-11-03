numero = int(input('Digite um número: '))
maior = numero
menor = numero
flag = str(input('Quer continuar: [s/n] ')).strip().upper()[0]
cont = 1
soma = numero
media = 0
while flag in 'Ss':
    num2 = int(input('Digite um número: '))
    if num2 > numero:
        maior = num2
    elif num2 < numero:
        num2 = menor
    soma += soma
    flag = str(input('Quer continuar: [s/n] ')).strip().upper()[0]
    cont += 1
media = soma / cont   # deixa fora do laço para não repetir sem necessidade
print(f'Você digitou {cont} números e a media foi {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
