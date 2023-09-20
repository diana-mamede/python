"""Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente."""
valores = [[], []]

for _ in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    elif valor % 2 != 0:
        valores[1].append(valor)

print(f"""
Pares: {sorted(valores[0])}
Impares{sorted(valores[1])}""")
