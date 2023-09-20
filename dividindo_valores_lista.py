"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""

numeros = []
impares = []
pares = []

while True:
    numero = int(input('Digite um número: '))

    if numero not in numeros:
        numeros.append(numero)
        if numero % 2 == 0:
            pares.append(numero)
            print('Adicionados a lista de numeros pares.')
        elif numero % 2 != 0:
            impares.append(numero)
            print('Adicionado a lista de numeros impares.')
    else:
        print('Valor duplicado.')

    continuar = str(input('Continuar? [S/N]: ')).upper().strip()[0]
    if 'N' in continuar:
        break

print('=' * 30)
print(f"""
Números adicionados a lista geral: {numeros}

Impares: {impares}

Pares: {pares}""")
