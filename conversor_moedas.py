# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quanto ela pode comprar de outras moedas.

real = float(input('Quanto você tem disponível em reais: R$'))
dolar = real/4.86
euro = real/5.30
libra = real/6.13
print(f'Com esse valor, você pode comprar US${dolar :.2f}.')
print(f'Com esse valor, você pode comprar €{euro :.2f}.')
print(f'Com esse valor, você pode comprar £{libra :.2f}.')
