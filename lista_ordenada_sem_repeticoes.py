"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
 já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

numeros = []
for _ in range(0, 5):
    numero = int(input('Digite um valor: '))
    if _ == 0 or numero > numeros[-1]:
        numeros.append(numero)
        print('Adicionado ao final da lista.')
    else:
        posicao = 0
        while posicao < len(numeros):
            if numero <= numeros[posicao]:
                numeros.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista.')
                break
            posicao += 1
print(numeros)
