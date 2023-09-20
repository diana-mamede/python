# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número inteiro: '))
divisores = 0
for x in range(1, numero + 1):
    if numero % x == 0:
        print('\033[34m', end=' ')
        divisores += 1
    else:
        print('\033[31m', end=' ')
    print(f'{x}', end=' ')
print(f'\n\033[m O numero {numero} foi divisível {divisores} vezes.')
if divisores == 2:
    print('Ele é primo.')
else:
    print('Ele não é primo.')
