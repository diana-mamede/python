"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e
vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""
from random import randint
print('*~' * 15)
print('Palpites de Jogos da Mega Sena')
print('*~' * 15)

lista = []
jogos = []
quantidade = int(input('Quantos jogos você quer? '))
total = 1

while total <= quantidade:
    contagem = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
        contagem+=1
        if contagem == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total+=1
for indice, l in enumerate(jogos):
    print(f'Jogo {indice+1}: {l}')
