# Conversão de Celsius
# objetivo é verificar na fórmula 2 que nem precisa de parenteses por ser a ordem de preferencia

celsius = float(input("Informe a temperatura em ºC: "))
# fahrenheit = ((celsius * 1.8) + 32)
fahrenheit = 9 * celsius / 5 + 32
print(f'A temperatura de {celsius}ºC corresponde a {fahrenheit}ºF.')

