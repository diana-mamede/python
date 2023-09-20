"""Faça um programa que calcule a soma entre
todos os números impares que sao multiplos de 3 e
estejam no intervalo entre 1 e 500"""

soma = 0
total_numeros = 0
for contagem in range(1, 500, 2):
    if contagem % 3 == 0:
        total_numeros += 1
        soma += contagem
print(f'A soma entre os {total_numeros} números impares multiplos de 3 no intervalo entre 1 e 500 é: {soma} ')
print('FIM.')
