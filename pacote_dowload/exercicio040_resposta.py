n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f"A média do aluno é {media:.1f} tirando nota {n1} e {n2}")
# if media >= 5 and media <= 7:

# OUTRO MODO DE APRESENTAR A CONDIÇÃO
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO!')
elif media >= 7:
    print('O aluno está APROVADO.')
