"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. """

valores = []
maior = menor = 0

for valor in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {valor}: ')))

    if valor == 0:
        menor = maior = valores[valor]
    else:
        if valores[valor] < menor:
            menor = valores[valor]
        elif valores[valor] > maior:
            maior = valores[valor]

print('-' * 40)
print(f'Foram digitados os valores {valores}')
print(f'O maior valor inserido foi {maior}, na posição', end=' ')
for indice, num in enumerate(valores):
    if num == maior:
        print(f'{indice}...', end=' ')
print(f'\nE o menor foi {menor}, na posição', end=' ')
for indice, num in enumerate(valores):
    if num == menor:
        print(f'{indice}...', end=' ')
