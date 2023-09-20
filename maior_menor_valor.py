# Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor.

primeiro_numero = input('Digite um numero: ')
segundo_numero = input('Digite mais um numero: ')
terceiro_numero = input('Digite o ultimo numero: ')

if segundo_numero < primeiro_numero > terceiro_numero:
    print(f'O maior número é: {primeiro_numero}')
elif primeiro_numero < segundo_numero > terceiro_numero:
    print(f'O maior número é: {segundo_numero}')
else:
    print(f'O maior número é: {terceiro_numero}')

if segundo_numero > primeiro_numero < terceiro_numero:
    print(f'O menor número é: {primeiro_numero}')
elif primeiro_numero > segundo_numero < terceiro_numero:
    print(f'O menor número é: {segundo_numero}')
else:
    print(f'O menor número é: {terceiro_numero}')
