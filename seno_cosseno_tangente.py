# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tagente.

import math
angulo = float(input('Digite o angulo que você deseja calcular: '))
seno = math.sin(math.radians(angulo))
print(f'O seno de {angulo} vale: {seno :.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O cosseno de {angulo} vale: {cosseno :.2f}')
tangente = math.tan(math.radians(angulo))
print(f'A tangente de {angulo} vale: {tangente :.2f}')
