# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as info possiveis sobre ele.

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('Possui apenas letras?', a.isalpha())
print('É um numero?', a.isnumeric())
print('Possui numeros e letras?', a.isalnum())
print('Está com letras maiúsculas?', a.isupper())
print('Está com letras minusculas?', a.islower())
print('Está capitalizada?', a.istitle())
