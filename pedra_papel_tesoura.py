# Crie um programa que jogue jokenpo.
import random
import time
print('=#=' * 20)
print('Vamos jogar Jokenpô!')
print('=#=' * 20)

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
jogador = int(input("""
Suas opções:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura
Qual sua jogada? 
"""))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)

print('=#=' * 20)
print(f'O computador escolheu {itens[computador]}!')
print(f'O jogador escolheu {itens[jogador]}!')
print('=#=' * 20)

if computador == jogador:
    print('EMPATE!')
elif (computador == 0 and jogador == 1) or (computador == 2 and jogador == 0) or (computador == 1 and jogador == 2):
    print('JOGADOR VENCEU!')
elif (computador == 1 and jogador == 0) or (computador == 0 and jogador == 2) or (computador == 2 and jogador == 1):
    print('COMPUTADOR VENCEU!')
