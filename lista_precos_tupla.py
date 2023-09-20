"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

livros = ('É assim que acaba', 44.90, 'Medo Clássico', 59.99,
          'A Hipótese do Amor', 35.30, 'A Mandibula de Caim', 50.26,
          'Box Povo do Ar', 206.90, 'O Sol é para todos', 69.90)

print('*' * 30)
print(f'{"L I V R A R I A" :^40}')
print('*' * 30)

for _ in range(0, len(livros)):
    if _ % 2 == 0:
        print(f'{livros[_] :.<40}', end=' ')
    if _ % 2 != 0:
        print(f'R${livros[_] :>5.2f}')
print('*' * 40)
