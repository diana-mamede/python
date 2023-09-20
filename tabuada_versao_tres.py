"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""

print('=' * 20)
print('TABUADA')
print('=' * 20)

while True:
    numero = int(input('Digite um valor para ver sua tabuada: '))
    if numero < 0:
        break
    for tabuada in range(1, 10+1):
        print(f'{numero} x {tabuada :2} = {numero * tabuada}')

print('*' * 30)
print('Fim do programa Tabuada. Volte sempre!')
print('*' * 30)
