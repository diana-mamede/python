"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

import random
numero_aleatorio = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
                    random.randint(1, 100), random.randint(1, 100))
print(f'Os valores sorteados foram: ', end='')
print(numero_aleatorio, sep=' , ')
print(f'O maior valor sorteado foi {max(numero_aleatorio)} e o menor foi {min(numero_aleatorio)}')
