# Crie um programa que leia o nome de uma pessoa e diga se em Silva.

nome = input(str('Digite o nome de alguém: ')).strip().upper().split()
print('Esse nome tem Silva?')
print('SILVA' in nome)
