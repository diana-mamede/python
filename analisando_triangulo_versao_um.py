# Faça um programa que leia 3 retas e diga ao usuario se elas podem ou não formar um triangulo.

print('Vamos construir um triangulo!\nDiga-me o valor de 3 retas para descobrirmos se elas podem formar um triangulo.')
primeira_reta = float(input('Digite o valor da primeira reta: '))
segunda_reta = float(input('Digite o valor da segunda reta: '))
terceira_reta = float(input('Digite o valor da ultima reta: '))
if primeira_reta + segunda_reta > terceira_reta:
    print('SIM! A combinação dessas retas forma um triangulo.')
else:
    print('AH, NÃO! Esses valores de retas não formam um triangulo.')
