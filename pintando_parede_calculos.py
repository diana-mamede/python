# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sendo que: 1L tinta = 2 m²

largura = float(input('Qual a largura da parede, em metros:'))
altura = float(input('Qual a altura da parede, em metros:'))
area = largura*altura
tinta = area/2
print(f'A quantidade de tinta necessaria para pintar uma parede de {area :.1f} m² é {tinta :.2f} l. ')
