"""Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

valores = []

while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não será adicionado.')
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break

print('=' * 30)
print(f'Os valores digitados foram {sorted(valores)}')
