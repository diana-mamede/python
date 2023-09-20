# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome 'Santo'.

cidade = input(str('Digite o nome de uma cidade: ')).strip()
print(cidade[0:5].upper() == 'SANTO')
