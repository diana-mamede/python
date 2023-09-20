"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quantos os números pares."""
import time

numeros = (int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),
           int(input('Digite um valor: ')))

print(f'Você digitou os valores: {numeros}')
print('. . .Analisando. . . ')
time.sleep(2)

par = 0
for _ in numeros:
    if _ % 2 == 0:
        par += 1

print(f'O valor 9 apareceu {numeros.count(9)} vezes. ')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}° posição.')
else:
    print('O valor 3 não foi digitado.')
print(f'Foram digitados {par} numeros pares.')
print('Fim!')
