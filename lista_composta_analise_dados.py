"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if 'N' in continuar:
        break

print(f'Foram adicionadas {len(pessoas)} pessoas.')
print(f'O menor peso foi de {menor :.1f}Kg. Peso de', end=' ')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'{pessoa[0]}', end=' ')
print(f'\nO maior peso foi de {maior :.1f}Kg. Peso de', end=' ')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'{pessoa[0]}', end=' ')
