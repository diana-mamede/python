"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

numeros = []
quantidade = 0

while True:
    numero = int(input('Digite um valor: '))

    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado.')
        quantidade += 1
    else:
        print('Valor duplicado.')

    continuar = str(input('Continuar? [S/N]')).strip().upper()[0]
    if 'N' in continuar:
        break

print(f"""
Foram adicionados {quantidade} valores.
Lista ordenada de forma decrescente: {sorted(numeros, reverse=True)}""")

if 5 in numeros:
    print('O valor 5 foi adicionado na lista.')
else:
    print('O valor 5 não foi adicionado na lista.')
