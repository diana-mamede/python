"""Melhore o jogo do df 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar
mostrando no final quantos palpites foram necessários para vencer."""

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

tentativas = 1
while aposta != numero_aleatorio:
    aposta = int(input('Não, não! Tente novamente: '))
    tentativas += 1
    if aposta > numero_aleatorio:
        print('Menos...')
    elif aposta < numero_aleatorio:
        print('Mais...')
print('=' * 20)
print(f'Uau, você venceu! Foram necessárias {tentativas} tentativas.')
