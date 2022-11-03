# Aluguel do Carro
# pergunte a quantidade de dias alugados
# pergunte a quantidade de quilômetros percorridos
# calcule sabendo (dia = R$ 60,00 e Km = 0.15)

dias_alugados = int(input('Informe a quantidade de dias de locação do veículo: '))
km_percorridos = int(input('Informe a quilometragem percorrida com o veículo: '))
valor_dias = dias_alugados * 60
valor_km = km_percorridos * 0.15
print(f'Considerando: \n'
      f'- {dias_alugados} dias de locação a R$ 60,00/diária \n'
      f'- {km_percorridos}/km percorridos a R$ 0,15/Km \n'
      f'  Valor discriminado para pagamento: \n'
      f'- Diária: R$ {valor_dias:.2f} \n'
      f'- Quilometragem: R$ {valor_km:.2f} \n'
      f'VALOR TOTAL: R$ {valor_dias + valor_km:.2f}')
