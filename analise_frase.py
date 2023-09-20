# Faça um programa que leia uma frase e mostre:
# Quantas vezes aparece a letra 'a'
# Em que posição ela aparece da primeira vez
# Em que posição ela aparece na última

frase = input(str('Digite uma frase qualquer: ')).strip().upper()
frase_correcao = frase.replace('á', 'a').replace('â', 'a').replace('à', 'a').replace('ã', 'a')
print('A letra a aparece essa quantidade de vezes: ', frase.count('A'))
print('A primeira aparição dessa letra é no indice: ', frase.find('A'))
print('A ultima aparição dessa letra é no indice: ', frase.rfind('A'))
