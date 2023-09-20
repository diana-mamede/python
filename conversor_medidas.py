# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metros = float(input('Escreva o tamanho em metros:'))
quilometro = metros/1000
centimetros = metros*100
milimetros = metros*1000
print(f'{metros} m equivalem a {quilometro}km, a {centimetros} cm e a {milimetros} mm')
