# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase para verificar se ela é um palíndromo: ')).strip().upper()
palavras = frase.split()
frase_sem_espacos = ''.join(palavras)
frase_inverso = ''

for letra in range(len(frase_sem_espacos) -1, -1, -1):
    frase_inverso += frase_sem_espacos[letra]
print(f'O inverso de {frase_sem_espacos} é {frase_inverso}')

if frase_inverso == frase_sem_espacos:
    print(f'A frase digitada é um palíndromo!')
else:
    print(f'A frase digitada não é um palíndromo!')
