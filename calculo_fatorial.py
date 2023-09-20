# Faça um programa que leia um número qualquer e mostre o seu fatorial:
from math import factorial
from time import sleep

numero = int(input('Digite um número inteiro: '))
fatorial = factorial(numero)
print(f'Calculando {numero}! =')
sleep(2)

while numero > 0:
    print(f'{numero}', end=' ')
    print(' x ' if numero > 1 else ' = ', end=' ')
    numero-= 1

print(f'{fatorial}')
print('Fim do programa. Volte sempre!')
