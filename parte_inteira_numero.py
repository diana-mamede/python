# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

numero = float(input('Digite um numero Real:'))
parte_inteira = int(numero)
print(f'A parte inteira de {numero} é {parte_inteira}')

# outra possivel forma utilizando a biblioteca math
from math import trunc
numero = float(input('Digite um numero Real:'))
print(f'A parte inteira de {numero} é {trunc(numero)}')
