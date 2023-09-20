# Escreva um programa que mostre uma contagem regressiva na tela para o estouro de fogos de artifício, indo de 10 ate 0, com uma pausa de 1 seg. entre eles.

import time
# import emoji
for contagem in range(10, 0, -1):
    print(contagem, '...')
    time.sleep(1)
print('FOGOS DE ARTIFICIO!🥳🎇')
