# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

soma = 0
quantidade_numeros = 0
for soma_pares in range(1, 7):
    numeros = int(input(f'Digite o {soma_pares}° número inteiro: '))
    if numeros % 2 == 0:
        soma += numeros
        quantidade_numeros += 1
print(f'A soma dos {quantidade_numeros} números pares dessa sequencia é: {soma}')
