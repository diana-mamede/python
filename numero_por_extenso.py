# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numero_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero_inteiro = int(input('Digite um número inteiro entre 0 e 20: '))
    if 0 <= numero_inteiro <= 20:
        break
print(f'A versão por extenso de {numero_inteiro} é:', end=' ')
print(numero_extenso[numero_inteiro])
