"""Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci."""

print('*' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('*' * 30)

termos = int(input('Quantos termos você quer mostrar? '))
termo_um = 0
termo_dois = 1
contagem = 3
print('=' * 30)
print(f'{termo_um} → {termo_dois}', end=' ')
while contagem <= termos:
    termo_tres = termo_um + termo_dois
    print(f'→ {termo_tres} ', end=' ')
    termo_um = termo_dois
    termo_dois = termo_tres
    contagem += 1
print('\nFim.')
