# Escreva um programa que converta uma temperatura digitada em °C para °F.

celcius = float(input('Qual a temperatura em celcius?'))
fahrenheit = (celcius * 9/5) + 32
print(f'{celcius} graus Celcius convertidos são: {fahrenheit} Fahrenheit')
