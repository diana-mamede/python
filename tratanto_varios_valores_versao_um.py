"""Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

numero = total = soma = 0

while numero != 999:
    numero = int(input('Digite um número inteiro [Digite 999 para parar]: '))
    total += 1
    soma += numero

print(f'O total de números inseridos foi {total - 1} e a soma desses números é {soma - 999}')
