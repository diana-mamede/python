""" Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """

import random
import time

print('#' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('#' * 30)

escolha_jogador = int(input("""
Oque você prefere?
[ 1 ] Impar
[ 2 ] Par
"""))

soma = 0
vitorias_jogador = 0

while True:
    print('^' * 30)
    numero_jogador = int(input('Digite o número que preferir: '))
    numero_computador = random.randint(1, 10)
    soma = numero_jogador + numero_computador

    print('PAR!')
    time.sleep(1)
    print('OU')
    time.sleep(1)
    print('IMPAR!')
    print('=' * 30)
    print(f'Você jogou {numero_jogador} e o computador jogou {numero_computador}. Total: {soma}.')
    print('=' * 30)

    if soma % 2 == 0:
        if escolha_jogador == 2:
            print('Uhu! Você venceu. Vamos mais uma vez!')
            vitorias_jogador += 1
        elif escolha_jogador == 1:
            print('Que pena... Pra você! Ganhei!')
            break

    if soma % 2 != 0:
        if escolha_jogador == 1:
            print('Uhu! Você venceu. Vamos mais uma vez!')
            vitorias_jogador += 1
        elif escolha_jogador == 2:
            print('Que pena... Pra você! Ganhei!')
            break

print('*~' * 20)
print(f'Você ganhou um total de {vitorias_jogador} vezes. Boa partida!')
print('*~' * 20)
