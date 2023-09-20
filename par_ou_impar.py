# Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR.

numero = int(input('Digite um numero inteiro qualquer: '))
print('='*20)
if numero % 2 == 0:
    print('Este número é par!')
else:
    print('Este número é impar!')
print('='*20)
