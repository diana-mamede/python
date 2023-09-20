# Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 e 5 e peça para o usuario descobrir qual o numero escolhido.
# O programa deverá escrever se o usuario vendeu ou perdeu

nome_jogador = input(str('Digite seu nome: '))
print(f'''Olá, {nome_jogador}, bem-vindo(a).
Um número entre 1 e 10 será sorteado.
Você deve tentar adivinhar qual foi o escolhido. 
Boa sorte! ''')

from random import randint
from time import sleep
numero_aleatorio = randint(1, 10)

print('~' * 20)
print('...Escolhendo...')
print('~' * 20)
sleep(3)
aposta = int(input('O computador escolheu um número, qual a sua aposta? '))
print('~' * 20)

if aposta == numero_aleatorio:
    print('Uau! Você ganhou, parabéns!')
else:
    print(f'Que pena, você perdeu. O numero escolhido foi {numero_aleatorio}. Quem sabe na próxima.')
