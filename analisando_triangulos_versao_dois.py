"""Refaça o desafio 035 dos triangulos, acrescente o recurso de mostrar que tipo de triangulo sera formado:
 - Equilatero: todos os lados iguais
 - Isosceles: dois lados iguais
 - Escaleno: todos os lados diferentes"""

# Df 35: Faça um programa que leia 3 retas e diga ao usuario se elas podem ou não formar um triangulo.

print('Vamos construir um triangulo!\nDiga-me o valor de 3 retas para descobrirmos se elas podem formar um triangulo e se sim, qual o tipo.')
primeira_reta = float(input('Digite o valor da primeira reta: '))
segunda_reta = float(input('Digite o valor da segunda reta: '))
terceira_reta = float(input('Digite o valor da terceira reta: '))
if primeira_reta < segunda_reta + terceira_reta and segunda_reta < primeira_reta + terceira_reta and terceira_reta < primeira_reta + segunda_reta:
    if primeira_reta == segunda_reta == terceira_reta:
        print('SIM! A combinação dessas retas forma um triangulo equilatero.')
    elif (primeira_reta == segunda_reta != terceira_reta) or (primeira_reta == terceira_reta != segunda_reta) or (segunda_reta == terceira_reta != primeira_reta):
        print('SIM! A combinação dessas retas forma um triangulo isosceles.')
    elif primeira_reta != segunda_reta != terceira_reta:
        print('SIM! A combinação dessas retas forma um triangulo escaleno.')
else:
    print('AH, NÃO! Esses valores de retas não formam um triangulo.')
