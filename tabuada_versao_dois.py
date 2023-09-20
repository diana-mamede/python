# Refaça o df 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um número inteiro qualquer para visualizar sua tabuada: '))
print('=' * 10)
for tabuada in range(1, 10+1):
    print(f'{numero} x {tabuada :2} = {numero * tabuada}')
print('=' * 10)
