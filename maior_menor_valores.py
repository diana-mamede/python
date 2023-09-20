""" Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""
valor = media = maior = menor = soma = total = 0
continuar = 'S'

while continuar == 'S':
    valor = int(input('Digite um valor: '))
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    soma += valor
    total += 1

    if total == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor

media = soma / total
print('*' * 30)
print(f"""
Total: {total}
Soma: {soma}
Média: {media}
Maior: {maior}
Menor: {menor}
""")
print('*' * 30)
