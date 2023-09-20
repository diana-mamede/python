# Faça um programa que leia o comprimento de um cateto oposto e do cateto adjacente de um triangulo, calcule e mostre a hipotenusa.

cat_oposto = float(input('Digite o valor do cateto oposto: '))
cat_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = (cat_oposto**2 + cat_adjacente**2)**(1/2)
print(f'O valor da hipotenusa é igual a: {hipotenusa :.2f}')

# Outra resolução utilizando a biblioteca math
from math import hypot
cat_oposto = float(input('Digite o valor do cateto oposto: '))
cat_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(cat_oposto, cat_adjacente)
print(f'O valor da hipotenusa é igual a: {hipotenusa :.2f} ')
