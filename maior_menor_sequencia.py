# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for sequencia in range(1, 6):
    peso = float(input(f'Digite o peso, em kg, da {sequencia}° pessoa: '))
    if sequencia == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi {maior :.1f}Kg')
print(f'O menor peso lido foi {menor :.1f}Kg')
