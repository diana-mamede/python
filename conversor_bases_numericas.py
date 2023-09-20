""" Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao:
1 - binario
2 - octal
3 - hexadecimal """

numero = int(input('Digite um número inteiro: '))
conversao = int(input("""
Escolha uma das bases de conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal
"""))
if conversao == 1:
    print(f'{numero} convertido para binário é equivalente a: {bin(numero) [2:]}')
elif conversao == 2:
    print(f'{numero} convertido para octal é equivalente a: {oct(numero) [2:]}')
elif conversao == 3:
    print(f'{numero} convertido para hexadecimal é equivalente a: {hex(numero) [2:]}')
else:
    print('O valor escolhido não corresponde com nenhuma das bases de conversão disponíveis.')
